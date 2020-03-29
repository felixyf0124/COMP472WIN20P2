
from vocabularyvalidator import VocabularyValidator as vv

class NGram:
    # constructor 
    # :param n: 1,2,3 
    def __init__(self,n:int):
        self.n = n
        self.table = dict()

    # private function 
    # generat 1-gram table in 1 level dict
    def __nGram1(self):
        self.table = dict()
    
    # private function 
    # generat 2-gram table in 2 level dict
    def __nGram2(self):
        self.table = dict(dict())

    # private function 
    # generat 3-gram table in 3 level dict
    def __nGram3(self):
        self.table = dict(dict(dict()))

    # private function 
    # feed 1-gram
    def __feed1gram(self,subStr):
        self.table[subStr] += 1

    # feed function 
    # feed a string if the string size equals to the n-gram size
    # else throw an expection
    # :param: subStr: str
    def feed(self, subStr:str):
        if(range(subStr)!= self.n):
            error ="Invalid feed: input feed length does not match the current n-gram size.\n"
            error += "input feed size: " + str(range(subStr)) + "\n"
            error += "current n-gram size: " + str(self.n) + "\n"
            raise Exception(error)
        else:
            if(self.n == 1):
                self.__feed1gram(subStr)


    