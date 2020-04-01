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

    # verify vocabulary type among the requirement types
    # return boolean if match the speicified type
    def verify(self, vocabulary: str, type: int):
        if(type == 0):
            return self.verify0(vocabulary)
        if(type == 1):
            return self.verify1(vocabulary)
        if(type == 2):
            return self.verify2(vocabulary)

    # add type 0 vocab set into dictionary
    def __addVocabSet0(self):
        vocabSet = set(string.ascii_lowercase)
        self.vocabSet[0] = vocabSet

    # add type 1 vocab set into dictionary
    def __addVocabSet1(self):
        vocabSet = set(string.ascii_letters)
        self.vocabSet[1] = vocabSet

    # add type 2 vocab set into dictionary
    # def __addVocabSet2(self):

        # default, encoding = locale.getdefaultlocale()
        # languages = [default] + ['en_US', 'fr_FR', 'es_ES']
        # lan = locale.getdefaultlocale('en_US',)
        # for language in languages:
        #     # data = LocaleData(language)
        #     # alphabet = data.getExemplarSet()
        #     # print(language, alphabet)
        # vocabSet = set(string.ascii_letters)

        # self.vocabSet[2] = vocabSet
