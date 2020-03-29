import re


class VocabularyValidator:
   
    # type 0: 
    # Fold the corpus to lowercase 
    # and use only the 26 letters of the alphabet [a-z]
    # return boolean
    def verify0(self, vocabulary:str):
        v = vocabulary.lower()
        for each in v:
            if (re.match(r"[a-z]", each) == None):
                return False
        return True

    # type 1: 
    # Distinguish up and low cases and 
    # use only the 26 letters of the alphabet [a-z, A-Z]
    # return boolean
    def verify1(self, vocabulary:str):
        v = vocabulary
        for each in v:
            if (re.match(r"[a-zA-Z]", each) == None):
                return False
        return True

    # type 2: 
    # Distinguish up and low cases and 
    # use all characters accepted by the built-in isalpha() method
    # return boolean
    def verify2(self, vocabulary:str):
        if (vocabulary.isalpha()):
            return True
        else:
            return False

    # verify vocabulary type among the requirement types
    # return boolean if match the speicified type
    def verify(self, vocabulary:str, type:int):
        if(type == 0):
            return self.verify0(vocabulary)
        if(type == 1):
            return self.verify1(vocabulary)
        if(type == 2):
            return self.verify2(vocabulary)
