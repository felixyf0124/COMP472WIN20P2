class Loader:
    # vocabularyLevel 0: Fold the corpus to lowercase and use only the 26 letters of the alphabet [a-z]
    # vocabularyLevel 1: Distinguish up and low cases and use only the 26 letters of the alphabet [a-z, A-Z]
    # vocabularyLevel 2: Distinguish up and low cases and use all characters accepted by the built-in isalpha() method
    # nGramSize: 1 = character unigrams, 2 = character bigrams, 3 = character trigrams
    # smoothingValue: real number representing the smoothing value
    # trainingPath: training path file
    # testingPath: testing path file
    def __init__(self, vocabularyLevel, nGramSize, smoothingValue, trainingPath, testingPath):
        print('vocabularyLevel: ', vocabularyLevel)
        print('nGramSize: ', nGramSize)
        print('smoothingValue: ', smoothingValue)

        trainingFile = open(trainingPath, "r", encoding="utf8")
        lineNum = 0
        for line in trainingFile:
            lineNum += 1
        print('Training Path:')
        print(lineNum)
        trainingFile.close()

        testingFile = open(testingPath, "r", encoding="utf8")
        lineNum = 0
        for line in testingFile:
            lineNum += 1
        print('Testing Path:')
        print(lineNum)
        testingFile.close()
