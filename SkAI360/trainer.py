from ngram import NGram as ng
from vocabularyvalidator import VocabularyValidator as vv


class Trainer:
    # V = vocabularyLevel 0: Fold the corpus to lowercase and use only the 26 letters of the alphabet [a-z]
    # V = vocabularyLevel 1: Distinguish up and low cases and use only the 26 letters of the alphabet [a-z, A-Z]
    # V = vocabularyLevel 2: Distinguish up and low cases and use all characters accepted by the built-in isalpha() method
    # n = nGramSize: 1 = character unigrams, 2 = character bigrams, 3 = character trigrams
    # delta = smoothingValue: real number representing the smoothing value
    def __init__(self, V: int, n: int, delta: float, verbose: bool = False):
        if((V < 0) & (V > 2)):
            raise Exception("Invalid param V: " +
                            str(V) + "\n")
        if((n < 1) & (n > 3)):
            raise Exception("Invalid param n: " +
                            str(n) + "\n")

        self.V = V
        self.n = n
        self.delta = delta
        keys = {"eu", "ca", "gl", "es", "en", "pt"}
        self.tab = dict()
        self.totalCount = dict()
        for key in keys:
            self.tab[key] = ng(V, n, delta)
            self.totalCount[key] = 0
        # self.tab = ng(V, n, delta)  # total base
        self.totalCount["all"] = 0

        self.verbose = verbose

        self.docCounts = dict()
        for key in keys:
            self.docCounts[key] = 0

    # return V
    def getV(self):
        return self.V

    # return n
    def getN(self):
        return self.n

    # return smooth value delta
    def getDelta(self):
        return self.delta

    # return a list of filtered data from the line str
    def __popFeedList(self, lineStr):
        popList = []
        if(len(lineStr) >= self.n):
            verifier = vv()
            for i in range(len(lineStr)-self.n):
                subStr = lineStr[i:i+self.n]
                if(verifier.verify(subStr, self.V)):
                    popList.append(subStr)
        return popList

    # feed str to n-gram table
    def __feed(self, data: str, language: str):
        self.tab[language].feed(data)
        self.totalCount[language] += 1
        self.totalCount["all"] += 1

    # feed line info
    def feedLineInfo(self, language: str, lineStr: str):
        self.docCounts[language] += 1
        if(self.V == 0):
            lineStr = lineStr.lower()
        filteredDateList = self.__popFeedList(lineStr)

        for each in filteredDateList:
            self.__feed(each, language)

    # get value from certain language table at key

    def get(self, key: str, language: str):
        return self.tab[language].get(key)

    # get total count feed for specific language

    def getTotalCount(self, language: str = None):
        if(language != None):
            return self.totalCount[language]
        else:
            return self.totalCount["all"]

    # get table size for specific language
    def getTableSize(self, language: str):
        return self.tab[language].getTableSize()

    # get doc count at specific language
    def getDocCount(self, language: str):
        return self.docCounts[language]

    # get total doc count
    def getTotalDocCount(self):
        ttlDocCount = 0
        for key in self.docCounts:
            ttlDocCount += self.docCounts[key]
        return ttlDocCount

    # get non appear total entry
    def getNonAppearTotalEntry(self, language):
        return self.tab[language].getNonAppearTotalEntry()
