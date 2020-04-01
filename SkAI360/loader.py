class Loader:
    # vocabularyLevel 0: Fold the corpus to lowercase and use only the 26 letters of the alphabet [a-z]
    # vocabularyLevel 1: Distinguish up and low cases and use only the 26 letters of the alphabet [a-z, A-Z]
    # vocabularyLevel 2: Distinguish up and low cases and use all characters accepted by the built-in isalpha() method
    # nGramSize: 1 = character unigrams, 2 = character bigrams, 3 = character trigrams
    # smoothingValue: real number representing the smoothing value
    # trainingPath: training path file
    # testingPath: testing path file
    def __init__(self, vocabularyLevel: int, nGramSize: int, smoothingValue, trainingPath, testingPath):
        if((vocabularyLevel < 0) & (vocabularyLevel > 2)):
            raise Exception("Invalid param vocabularyLevel: " +
                            str(vocabularyLevel) + "\n")
        self.V = vocabularyLevel
        if((nGramSize < 1) & (vocabularyLevel > 3)):
            raise Exception("Invalid param nGramSize: " +
                            str(nGramSize) + "\n")
        self.n = nGramSize
        self.trainingPath = trainingPath
        self.testingPath = testingPath

        print('vocabularyLevel: ', vocabularyLevel)
        print('nGramSize: ', nGramSize)
        print('smoothingValue: ', smoothingValue)

        self.trainingData = dict()
        trainingFile = open(trainingPath, "r", encoding="utf8")
        lineNum = 0
        for line in trainingFile:
            if(len(line) > 0):
                lineNum += 1
                splited = line.split("\t", 3)
                self.trainingData[lineNum] = splited
        print('Training Path:')
        print(lineNum)
        trainingFile.close()

        self.testingData = dict()
        testingFile = open(testingPath, "r", encoding="utf8")
        lineNum = 0
        for line in testingFile:
             if(len(line) > 0):
                    lineNum += 1
                splited = line.split("\t", 3)
                self.testingFile[lineNum] = splited
        print('Testing Path:')
        print(lineNum)
        testingFile.close()
        
        self.lineCursor = 0;

    # reset lineCurser = 0
    def resetLineCursor(self):
        self.lineCursor = 0

    # get next line in trainingData
    def getNextLineInTrainingData(self):
        self.lineCursor += 1
        return self.trainingData[self.lineCursor]

    # get next line in testingData
    def getNextLineInTestingData(self):
        self.lineCursor += 1
        return self.testingData[self.lineCursor] 
