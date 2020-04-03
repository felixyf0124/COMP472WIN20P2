from ngram import NGram as ng
from vocabularyvalidator import VocabularyValidator as vv


class Trainer:
    # V = vocabularyLevel 0: Fold the corpus to lowercase and use only the 26 letters of the alphabet [a-z]
    # V = vocabularyLevel 1: Distinguish up and low cases and use only the 26 letters of the alphabet [a-z, A-Z]
    # V = vocabularyLevel 2: Distinguish up and low cases and use all characters accepted by the built-in isalpha() method
    # n = nGramSize: 1 = character unigrams, 2 = character bigrams, 3 = character trigrams
    # delta = smoothingValue: real number representing the smoothing value
    def __init__(self, V: int, n: int, delta: float):
        if((V < 0) & (V > 2)):
            raise Exception("Invalid param V: " +
                            str(V) + "\n")
        if((n < 1) & (n > 3)):
            raise Exception("Invalid param n: " +
                            str(n) + "\n")

        self.V = V
        self.n = n
        self.delta = delta
        self.tab = ng(V, n, delta)  # total base
        self.euTab = ng(V, n, delta)  # Basque
        self.caTab = ng(V, n, delta)  # Catalan
        self.glTab = ng(V, n, delta)  # Galician
        self.esTab = ng(V, n, delta)  # Spanish
        self.enTab = ng(V, n, delta)  # English
        self.ptTab = ng(V, n, delta)  # Portuguese

        self.ttlCount = 0
        self.euTtlCount = 0
        self.caTtlCount = 0
        self.glTtlCount = 0
        self.esTtlCount = 0
        self.enTtlCount = 0
        self.ptTtlCount = 0

        keys = {"eu", "ca", "gl", "es", "en", "pt"}
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

    # feed total base table
    def __feedBase(self, data: str):
        self.tab.feed(data)
        self.ttlCount += 1

    # feed Basque table
    def __feedEU(self, data: str):
        self.euTab.feed(data)
        self.euTtlCount += 1

    # feed Catalan table
    def __feedCA(self, data: str):
        self.caTab.feed(data)
        self.caTtlCount += 1

    # feed Galician table
    def __feedGL(self, data: str):
        self.glTab.feed(data)
        self.glTtlCount += 1

    # feed Spanish table
    def __feedES(self, data: str):
        self.esTab.feed(data)
        self.esTtlCount += 1

    # feed English table
    def __feedEN(self, data: str):
        self.enTab.feed(data)
        self.enTtlCount += 1

    # feed Portuguese table
    def __feedPT(self, data: str):
        self.ptTab.feed(data)
        self.ptTtlCount += 1

    def feedLineInfo(self, language: str, lineStr: str):
        self.docCounts[language] += 1
        if(self.V == 0):
            lineStr = lineStr.lower()
        filteredDateList = self.__popFeedList(lineStr)

        # feed Basque table
        if(language == "eu"):
            for each in filteredDateList:
                self.__feedEU(each)
                self.__feedBase(each)

        # feed Catalan table
        if(language == "ca"):
            for each in filteredDateList:
                self.__feedCA(each)
                self.__feedBase(each)

        # feed Galician table
        if(language == "gl"):
            for each in filteredDateList:
                self.__feedGL(each)
                self.__feedBase(each)

        # feed Spanish table
        if(language == "es"):
            for each in filteredDateList:
                self.__feedES(each)
                self.__feedBase(each)

        # feed English table
        if(language == "en"):
            for each in filteredDateList:
                self.__feedEN(each)
                self.__feedBase(each)

        # feed Portuguese table
        if(language == "pt"):
            for each in filteredDateList:
                self.__feedPT(each)
                self.__feedBase(each)

    # get value from base n-gram table at key
    def getFromBase(self, key: str):
        return self.euTab.get(key)

    # get value from EU n-gram table at key
    def getFromEU(self, key: str):
        return self.euTab.get(key)

    # get value from CA n-gram table at key
    def getFromCA(self, key: str):
        return self.caTab.get(key)

    # get value from GL n-gram table at key
    def getFromGL(self, key: str):
        return self.glTab.get(key)

    # get value from ES n-gram table at key
    def getFromES(self, key: str):
        return self.esTab.get(key)

    # get value from EN n-gram table at key
    def getFromEN(self, key: str):
        return self.enTab.get(key)

    # get value from PT n-gram table at key
    def getFromPT(self, key: str):
        return self.ptTab.get(key)

    # get value from certain language table at key
    def get(self, key: str, language: str):
        if(language == "eu"):
            return self.getFromEU(key)
        if(language == "ca"):
            return self.getFromCA(key)
        if(language == "gl"):
            return self.getFromGL(key)
        if(language == "es"):
            return self.getFromES(key)
        if(language == "en"):
            return self.getFromEN(key)
        if(language == "pt"):
            return self.getFromPT(key)

    # get total count feed for specific language
    def getTTLCount(self, language: str):
        if(language == "eu"):
            return self.euTtlCount
        if(language == "ca"):
            return self.caTtlCount
        if(language == "gl"):
            return self.glTtlCount
        if(language == "es"):
            return self.esTtlCount
        if(language == "en"):
            return self.enTtlCount
        if(language == "pt"):
            return self.ptTtlCount

    # get table size for specific language
    def getTableSize(self, language: str):
        if(language == "eu"):
            return self.euTab.getTableSize()
        if(language == "ca"):
            return self.caTab.getTableSize()
        if(language == "gl"):
            return self.glTab.getTableSize()
        if(language == "es"):
            return self.esTab.getTableSize()
        if(language == "en"):
            return self.enTab.getTableSize()
        if(language == "pt"):
            return self.ptTab.getTableSize()

    # get doc count at specific language
    def getDocCount(self, language: str):
        return self.docCounts[language]

    # get total doc count
    def getTotalDocCount(self):
        ttlDocCount = 0
        for key in self.docCounts:
            ttlDocCount += self.docCounts[key]
        return ttlDocCount
