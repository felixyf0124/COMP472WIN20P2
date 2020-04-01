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

    # get EU score
    def getEUScore(self, lineStr: str):
        nonAppear = 0
        chunkList = self.__popChunkList(lineStr)
        logDict = dict()
        for each in chunkList:
            counter = self.trainer.get(each, "eu")
            if(counter != None):
                logDict[each] = counter
            else:
                nonAppear += 1
        # not finished
