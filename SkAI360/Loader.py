class Loader:
    def __init__(self, vocabularyLevel, nGramSize, smoothingValue, trainingPath, testingPath):
        print('vocabularyLevel: ', vocabularyLevel)
        print('nGramSize: ', nGramSize)
        print('smoothingValue: ', smoothingValue)

        trainingFile = open(trainingPath, "r")
        lineNum = 0
        for line in trainingFile:
            lineNum += 1
        print('Training Path:')
        print(lineNum)
        trainingFile.close()

        testingFile = open(testingPath, "r")
        lineNum = 0
        for line in testingFile:
            lineNum += 1
        print('Testing Path:')
        print(lineNum)
        testingFile.close()
