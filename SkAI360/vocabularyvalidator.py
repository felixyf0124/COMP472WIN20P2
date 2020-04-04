import string


class VocabularyValidator:

    def __init__(self):
        self.vocabSet = dict()
        self.__addVocabSet0()
        self.__addVocabSet1()

    # type 0:
    # Fold the corpus to lowercase
    # and use only the 26 letters of the alphabet [a-z]
    # return boolean
    def verify0(self, vocabulary: str):
        v = vocabulary.lower()
        for each in v:
            if (each not in self.vocabSet[0]):
                return False
        return True

    # type 1:
    # Distinguish up and low cases and
    # use only the 26 letters of the alphabet [a-z, A-Z]
    # return boolean
    def verify1(self, vocabulary: str):
        v = vocabulary
        for each in v:
            if (each not in self.vocabSet[1]):
                return False
        return True

    # type 2:
    # Distinguish up and low cases and
    # use all characters accepted by the built-in isalpha() method
    # return boolean
    def verify2(self, vocabulary: str):
        if (vocabulary.isalpha()):
            return True
        else:
            return False

    # verify with extra consideration
    def verifyE(self, vocabulary: str, type: int):
        v = vocabulary
        isLastCharSpace = False
        for each in v:
            # check non-continuous space
            if (isLastCharSpace & each.isspace()):
                return False
            if(type == 0):
                if not (self.verify0(each) | each.isspace()):
                    return False
            if(type == 1):
                if not (self.verify1(each) | each.isspace()):
                    return False
            if(type == 2):
                if not (self.verify2(each) | each.isspace()):
                    return False

            if (each.isspace()):
                isLastCharSpace = True
            else:
                isLastCharSpace = False
        return True

    # verify vocabulary type among the requirement types
    # return boolean if match the speicified type
    def verify(self, vocabulary: str, vType: int, extra: int = 0):
        if(extra == 1) & (len(vocabulary) > 1):
            return self.verifyE(vocabulary, vType)
        else:
            if(vType == 0):
                return self.verify0(vocabulary)
            if(vType == 1):
                return self.verify1(vocabulary)
            if(vType == 2):
                return self.verify2(vocabulary)

    # add type 0 vocab set into dictionary
    def __addVocabSet0(self):
        vocabSet = set(string.ascii_lowercase)
        self.vocabSet[0] = vocabSet

    # add type 1 vocab set into dictionary
    def __addVocabSet1(self):
        vocabSet = set(string.ascii_letters)
        self.vocabSet[1] = vocabSet

    # return vocab. set
    def getVocabSet(self, id: int):
        if(id in self.vocabSet):
            return self.vocabSet[id]
