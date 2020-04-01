
from vocabularyvalidator import VocabularyValidator as vv


class NGram:
    # constructor
    # :param V: 0,1,2
    # :param n: 1,2,3
    def __init__(self, V: int, n: int, delta: float):
        if((V < 0) & (V > 2)):
            raise Exception("Invalid param V: " + str(V) + "\n")

        self.V = V
        self.n = n
        self.delta = delta
        self.table = dict()
        if(self.n == 1):
            self.__nGram1()
        elif(self.n == 2):
            self.__nGram2()
        elif(self.n != 3):
            # n = 3 while be realtime dynamic initialize
            # but if n ! = 1 or 2 or 3 then invalid input
            raise Exception("Invalid param n: " + str(n) + "\n")

    # private function
    # generat 1-gram table in 1 level dict
    def __nGram1(self):
        if(self.V == 0):
            vocabSet = vv().vocabSet[0]
            for x in vocabSet:
                self.table[x] = 0
        if(self.V == 1):
            vocabSet = vv().vocabSet[1]
            for x in vocabSet:
                self.table[x] = 0

    # private function
    # generat 2-gram table in 2 level dict
    def __nGram2(self):
        if(self.V == 0):
            vocabSet = vv().vocabSet[0]
            for x in vocabSet:
                self.table[x] = dict()
                for y in vocabSet:
                    self.table[x][y] = 0

        if(self.V == 1):  # initial for v == 1
            vocabSet = vv().vocabSet[1]
            for x in vocabSet:
                self.table[x] = dict()
                for y in vocabSet:
                    self.table[x][y] = 0

    # private function
    # generat 3-gram table in 3 level dict
    def __nGram3(self):
        if(self.V == 0):
            vocabSet = vv().vocabSet[0]
            for x in vocabSet:
                self.table[x] = dict()
                for y in vocabSet:
                    self.table[x][y] = dict()
                    for z in vocabSet:
                        self.table[x][y][z] = 0

        if(self.V == 1):  # initial for v == 1
            vocabSet = vv().vocabSet[1]
            for x in vocabSet:
                self.table[x] = dict()
                for y in vocabSet:
                    self.table[x][y] = dict()
                    for z in vocabSet:
                        self.table[x][y][z] = 0

    # private function
    # feed 1-gram
    def __feed1Gram(self, subStr: str):
        # v = 2 and the element is not initialized
        # then initalize
        if((self.V == 2) & (subStr not in self.table)):
            self.table[subStr] = 0

        self.table[subStr] += 1

    # private function
    # feed 2-gram
    def __feed2Gram(self, subStr: str):
        # v = 2 and the element is not initialized
        # then initalize
        if(self.V == 2):
            if(subStr[0] not in self.table):
                self.table[subStr[0]] = dict()
            if(subStr[1] not in self.table[subStr[0]]):
                self.table[subStr[0]][subStr[1]] = 0

        self.table[subStr[0]][subStr[1]] += 1

    # private function
    # feed 3-gram
    def __feed3Gram(self, subStr: str):
        # v = 2 and the element is not initialized
        # then initalize
        if(self.V == 2):
            if(subStr[0] not in self.table):
                self.table[subStr[0]] = dict()
            if(subStr[1] not in self.table[subStr[0]]):
                self.table[subStr[0]][subStr[1]] = dict()
            if(subStr[2] not in self.table[subStr[0]][subStr[1]]):
                self.table[subStr[0]][subStr[1]][subStr[2]] = 0

        self.table[subStr[0]][subStr[1]][subStr[2]] += 1

    # feed function
    # feed a string if the string size equals to the n-gram size
    # else throw an expection
    # :param: subStr: str
    def feed(self, subStr: str):
        if(len(subStr) != self.n):
            error = "Invalid feed: input feed length does not match the current n-gram size.\n"
            error += "input feed size: " + str(range(subStr)) + "\n"
            error += "current n-gram size: " + str(self.n) + "\n"
            raise Exception(error)
        else:
            if(self.n == 1):
                self.__feed1Gram(subStr)
            if(self.n == 2):
                self.__feed2Gram(subStr)
            if(self.n == 3):
                self.__feed3Gram(subStr)
