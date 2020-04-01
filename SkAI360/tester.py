from ngram import NGram as ng
from vocabularyvalidator import VocabularyValidator as vv
from trainer import Trainer
import math
import copy


class Tester:

    def __init__(self, trainer: Trainer):
        self.trainer = copy.deepcopy(Trainer)

    def classify(self, lineStr: str):
        # self.trainer.
        pass

    def __popChunkList(self, lineStr: str):
        popList = []
        n = self.trainer.n
        V = self.trainer.V
        if(len(lineStr) >= n):
            verifier = vv()
            for i in range(len(lineStr)-n):
                subStr = lineStr[i:i+n]
                if(verifier.verify(subStr, V)):
                    popList.append(subStr)
        return popList

    # P(A|B) = P(A∩B)/P(B)
    def naiveBayes(self, a, b):
        pass

    # get score of specific language
    def getScore(self, language: str, lineStr: str):
        nonAppear = 0
        chunkList = self.__popChunkList(lineStr)
        letterList = []
        smoothDelta = self.trainer.delta
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
