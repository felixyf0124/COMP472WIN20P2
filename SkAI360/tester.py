from ngram import NGram as ng
from vocabularyvalidator import VocabularyValidator as vv
from trainer import Trainer
import math
import copy


class Tester:

    def __init__(self, trainer: Trainer):
        self.trainer = trainer
        self.tracer = dict()
        self.lineCursor = 0
        self.correct = 0
        self.wrong = 0

    def classify(self, lineStr: str):
        scores = []
        scores.append(["eu", self.getScore("eu", lineStr)])
        scores.append(["ca", self.getScore("ca", lineStr)])
        scores.append(["gl", self.getScore("gl", lineStr)])
        scores.append(["es", self.getScore("es", lineStr)])
        scores.append(["en", self.getScore("en", lineStr)])
        scores.append(["pt", self.getScore("pt", lineStr)])
        return sorted(scores, key=lambda score: score[1], reverse=False)

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

    # P(A|B) = P(A∩B)/P(B)
    def naiveBayes(self, anb, b):
        return anb/b

    # get score of specific language
    def getScore(self, language: str, lineStr: str):
        nonAppear = 0
        chunkList = self.__popChunkList(lineStr)
        letterList = []
        smoothDelta = self.trainer.getDelta()
        for each in chunkList:
            counter = self.trainer.get(each, language)
            if(counter != None):
                letterList[each] = counter + smoothDelta
            else:
                nonAppear += 1
        if(nonAppear > 0):
            ttlSoomthed = (self.trainer.getTableSize(language)+1) * smoothDelta
        else:
            ttlSoomthed = (self.trainer.getTableSize(language)) * smoothDelta
        score = 0
        for each in letterList:
            score += math.log10((letterList + smoothDelta)/ttlSoomthed)

        if(nonAppear > 0):
            for x in range(nonAppear):
                score += math.log10(smoothDelta/ttlSoomthed)
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

    # generate file name
    def generateFileName(self):
        filename = ""
        filename += 'trace_' + str(self.trainer.getV())
        filename += '_' + str(self.trainer.getN())
        filename += '_' + str(self.trainer.getDelta()) + '.txt'
        return filename

    def getTotalLineSize(self):
        return len(self.tracer)

    def getLineCursorPos(self):
        return self.lineCursor

    def getAccuracy(self):
        return str((self.correct)/(self.correct + self.wrong) * 100) + '%'
