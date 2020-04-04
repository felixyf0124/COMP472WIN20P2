from loader import Loader as ld

trainingFile = "dataset/training-tweets.txt"
testingFile = "dataset/test-tweets-given.txt"

loader = ld(0, 1, 0.1, trainingFile, testingFile)
