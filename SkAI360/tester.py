from ngram import NGram as ng
from vocabularyvalidator import VocabularyValidator as vv
from trainer import Trainer
from metrics import Metrics
from writer import Writer
import math
import copy


class Tester:

    def __init__(self, trainer: Trainer):
        self.trainer = trainer
        self.tracer = dict()
        self.metrics = Metrics()
        self.lineCursor = 0

        self.correct = 0
        self.wrong = 0

        self.verbose = trainer.verbose
        # if(self.verbose):
        #     # print(self.trainer.tab.table)

    # get all
    def classify(self, lineStr: str):
        scores = []
        scores.append(["eu", self.getScore("eu", lineStr)])
        scores.append(["ca", self.getScore("ca", lineStr)])
        scores.append(["gl", self.getScore("gl", lineStr)])
        scores.append(["es", self.getScore("es", lineStr)])
        scores.append(["en", self.getScore("en", lineStr)])
        scores.append(["pt", self.getScore("pt", lineStr)])
        scores = sorted(scores, key=lambda score: score[1], reverse=True)
        # print(scores)
        # if(self.verbose):
        #     print('SCORES')
        #     for s in scores:

        return scores

    # return a list of chopped substr
    def __popChunkList(self, lineStr: str):
        popList = []
        n = self.trainer.getN()
        V = self.trainer.getV()
        if(len(lineStr) >= n):
            verifier = vv()
            for i in range(len(lineStr)-n):
                subStr = lineStr[i:i+n]
                if(verifier.verify(subStr, V)):
                    popList.append(subStr)
        return popList

    # get score of specific language
    def getScore(self, language: str, lineStr: str):
        nonAppear = 0
        chunkList = self.__popChunkList(lineStr)
        letterList = []
        smoothDelta = self.trainer.getDelta()
        for each in chunkList:
            counter = self.trainer.get(each, language)
            # print(counter)
            if(counter != None):
                letterList.append(counter + smoothDelta)
            else:
                nonAppear += 1

        # print(chunkList)
        # print(letterList)
        # nonAppear = 0
        if(nonAppear > 0):
            ttlSoomthed = (self.trainer.getTableSize(
                language)+1-self.trainer.getNonAppearTotalEntry(language)) * smoothDelta
        else:
            ttlSoomthed = (self.trainer.getTableSize(
                language)-self.trainer.getNonAppearTotalEntry(language)) * smoothDelta

        totalFeed = self.trainer.getTotalCount(language)

        # start with prior
        score = math.log10(self.trainer.getDocCount(
            language)/self.trainer.getTotalDocCount())

        for each in letterList:
            if(each != 0):
                score += math.log10((each + smoothDelta) /
                                    (totalFeed + ttlSoomthed))

        if(nonAppear > 0) & (smoothDelta > 0):
            for x in range(nonAppear):
                score += math.log10(smoothDelta/(totalFeed + ttlSoomthed))
        return score

    def doTestLine(self, line: [], atLine: int):
        scores = self.classify(line[3])
        # print(scores)
        classifiedLan = scores[0][0]
        score = scores[0][1]
        if(classifiedLan == line[2]):
            correctness = "correct"
            self.correct += 1
        else:
            correctness = "wrong"
            self.wrong += 1
        # (tweet id, most likely class, score of the most likely class, correctness label)
        self.tracer[atLine] = [line[0], classifiedLan,
                               score,  line[2], correctness]
        self.metrics.update(line[2], classifiedLan)

    def getNextLinesString(self, numOfLines: int = 1):
        content = ""
        count = 0
        while((count < numOfLines) & (self.lineCursor + 1 in self.tracer)):
            self.lineCursor += 1
            count += 1
            line = self.tracer[self.lineCursor]
            content += line[0]+"\t"
            content += line[1]+"\t"
            # score
            content += self.format_e(line[2])+"\t"
            content += line[3]+"\t"
            content += line[4]+"\n"

        return content

    # return a format of e scientific
    def format_e(self, n):
        formated = '{:.2e}'.format(n)
        return formated

    # reset trace line cursor at line (default 0)
    def resetTraceCursor(self, atLine: int = 0):
        self.lineCursor = atLine

    # generate trace file name
    def generateTraceFileName(self):
        filename = ""
        filename += 'trace_' + str(self.trainer.getV())
        filename += '_' + str(self.trainer.getN())
        filename += '_' + str(self.trainer.getDelta()) + '.txt'
        return filename

    # generate evaluation file name
    def generateEvalFileName(self):
        filename = ""
        filename += 'eval_' + str(self.trainer.getV())
        filename += '_' + str(self.trainer.getN())
        filename += '_' + str(self.trainer.getDelta()) + '.txt'
        return filename

    def getTotalLineSize(self):
        return len(self.tracer)

    def getLineCursorPos(self):
        return self.lineCursor

    def getAccuracy(self):
        accuracy = self.metrics.getAccuracy()
        if(accuracy != None):
            return "{:3.2f}".format(accuracy*100) + " %"
        else:
            return accuracy

    # do analyze after done test
    def analyze(self):
        if(len(self.metrics.analysis) == 0):
            self.metrics.analyze()

    # get formated str from result pack
    def getFormated(self, pack, key1: str, key2: str = ""):
        if(key2 != ""):
            value = pack[key1][key2]
        else:
            value = pack[key1]
        if(type(value) is str):
            return value
        else:
            return "{:1.4f}".format(value)

    # return formated analysis result in str
    def getAnalysisResult(self):
        outStr = ""
        self.analyze()
        result = self.metrics.getAnalysisResult()
        outStr += "{:1.4f}".format(result["accuracy"]) + "\n"
        precision = ""
        recall = ""
        f1 = ""
        keys = ["eu", "ca", "gl", "es", "en", "pt"]
        tab = "\t"
        for key in keys:
            precision += self.getFormated(result, "precision", key) + tab
            recall += self.getFormated(result, "recall", key) + tab
            f1 += self.getFormated(result, "f1Measure", key) + tab

        outStr += precision + "\n"
        outStr += recall + "\n"
        outStr += f1 + "\n"

        outStr += self.getFormated(result, "macroF1") + tab
        outStr += self.getFormated(result, "weightedAverageF1") + tab

        return outStr

    # output result
    def dumpResult(self):
        # dump trace data
        writer = Writer(self.generateTraceFileName())
        self.resetTraceCursor()

        writer.overwrite(self.getNextLinesString(800))
        while(self.getLineCursorPos() < self.getTotalLineSize()):
            writer.writeAtEOF(self.getNextLinesString(800))

        # dump analysis result data
        writer = Writer(self.generateEvalFileName())
        writer.overwrite(self.getAnalysisResult())
