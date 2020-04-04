import os


class Loader:
    # trainingPath: training path file
    # testingPath: testing path file
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.trainingPath = "./trainingDataSet/"
        self.testingPath = "./testingDataSet/"
        self.listOfTrainingFiles = os.listdir(self.trainingPath)
        self.listOfTestingFiles = os.listdir(self.testingPath)

        self.trainingData = dict()
        for each in self.listOfTrainingFiles:
            path = self.trainingPath + each
            if(os.path.isfile(path)):
                self.loadTrainingData(path, verbose)

        self.testingData = dict()
        count = 0
        for each in self.listOfTestingFiles:
            if count > 1:
                break
            path = self.testingPath + each
            if(os.path.isfile(path)):
                self.loadTestingData(path, verbose)
                count += 1

        self.lineCursor = 0

    # load training data into training data dict (cumulative load)
    def loadTrainingData(self, trainingPath: str, verbose: bool = False):

        trainingFile = open(trainingPath, "r", encoding="utf8")
        lineNum = len(self.trainingData)
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

    # load testing data into testing data dict (reset dict)
    def loadTestingData(self, testingPath: str, verbose: bool = False):
        self.testingData = dict()
        testingFile = open(testingPath, "r", encoding="utf8")
        lineNum = len(self.testingData)
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

    # get line cursor index position
    def getLineCursorPos(self):
        return self.lineCursor
