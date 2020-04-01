from ngram import NGram as ng
from vocabularyvalidator import VocabularyValidator as vv


class Trainer:
    def __init__(self, V: int, n: int, delta: float):
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

    # feed Basque table
    def __feedEU(self, data: str):
        self.euTab.feed(data)

    # feed Catalan table
    def __feedCA(self, data: str):
        self.caTab.feed(data)

    # feed Galician table
    def __feedGL(self, data: str):
        self.glTab.feed(data)

    # feed Spanish table
    def __feedES(self, data: str):
        self.esTab.feed(data)

    # feed English table
    def __feedEN(self, data: str):
        self.enTab.feed(data)

    # feed Portuguese table
    def __feedPT(self, data: str):
        self.ptTab.feed(data)

    # feed Spanish table
    def __feedEU(self, data: str):
        self.euTab.feed(data)

    def feedLineInfo(self, language: str, lineStr: str):
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
