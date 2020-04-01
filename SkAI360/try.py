import string
import locale
from vocabularyvalidator import VocabularyValidator as vv
from ngram import NGram
from loader import Loader as ld

vValidator = vv()

# print(vValidator.verify('a?',0))
# print(vValidator.verify('aA',0))
# print(vValidator.verify('a_a',0))
# print(vValidator.verify('_a/?',0))
# print(vValidator.verify('a?',1))
# print(vValidator.verify('a_a',1))
# print(vValidator.verify('AazB',1))
print(vValidator.verify('é', 1))
# print(vValidator.verify('a_a',2))
# print(vValidator.verify('_a/?',2))
# print('A2/'.lower())

ng1 = NGram(2, 3, 1)

ng1.feed("abc")
ng1.feed("abc")
ng1.feed("ayé")

print(ng1.table)
i = 0
# for each in vValidator.vocabSet[1]:
#     print(each)
#     i+=1
#     print(i)

trainingFile = "dataset/training-tweets.txt"
testingFile = "dataset/test-tweets-given.txt"

loader = ld(0, 1, 0.1, trainingFile, testingFile)
loader.resetLineCursor()
line = loader.getNextLineInTrainingData()
print(line)
