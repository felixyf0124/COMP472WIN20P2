class Loader:
    # trainingPath: training path file
    # testingPath: testing path file
    def __init__(self, trainingPath, testingPath, verbose: bool):
        self.verbose = verbose
        self.trainingData = dict()
        trainingFile = open(trainingPath, "r", encoding="utf8")
        lineNum = 0
        for line in trainingFile:
            line = line.rstrip('\n')
            if(len(line) > 0):
                lineNum += 1
                splited = line.split("\t", 3)
                self.trainingData[lineNum] = splited
        if(self.verbose):
            print('Training Path:')
            print(lineNum)
        trainingFile.close()

        self.testingData = dict()
        testingFile = open(testingPath, "r", encoding="utf8")
        lineNum = 0
        for line in testingFile:
            line = line.rstrip('\n')
            if(len(line) > 0):
                lineNum += 1
                splited = line.split("\t", 3)
                self.testingData[lineNum] = splited
        if(self.verbose):
            print('Testing Path:')
            print(lineNum)
        testingFile.close()

        self.lineCursor = 0

    # reset lineCurser = 0
    def resetLineCursor(self):
        self.lineCursor = 0

    # get next line in trainingData
    def getNextLineInTrainingData(self):
        self.lineCursor += 1
        return self.trainingData.get(self.lineCursor, None)

    # get a specific line in trainingData
    def getLineInTrainingData(self, n: int):
        return self.trainingData.get(n, None)

    # get next line in testingData
    def getNextLineInTestingData(self):
        self.lineCursor += 1
        return self.testingData.get(self.lineCursor, None)

    # get a specific line in trainingData
    def getLineInTestingData(self, n: int):
        return self.testingData.get(n, None)
