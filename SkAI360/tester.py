from ngram import NGram as ng
from vocabularyvalidator import VocabularyValidator as vv
from trainer import Trainer
import math
import copy


class Tester:

    def __init__(self, trainer: Trainer):
        self.trainer = trainer

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
