import math
import string
import locale
from vocabularyvalidator import VocabularyValidator as vv
from ngram import NGram
from loader import Loader as ld
from trainer import Trainer

# vValidator = vv()

# print(vValidator.verify('a?',0))
# print(vValidator.verify('aA',0))
# print(vValidator.verify('a_a',0))
# print(vValidator.verify('_a/?',0))
# print(vValidator.verify('a?',1))
# print(vValidator.verify('a_a',1))
# print(vValidator.verify('AazB',1))
# print(vValidator.verify('é', 1))
# print(vValidator.verify('a_a',2))
# print(vValidator.verify('_a/?',2))
# print('A2/'.lower())

# ng1 = NGram(2, 3, 1)

# ng1.feed("abc")
# ng1.feed("abc")
# ng1.feed("ayé")

# print(ng1.table)
# i = 0
# for each in vValidator.vocabSet[1]:
#     print(each)
#     i+=1
#     print(i)

trainingFile = "dataset/training-tweets.txt"
testingFile = "dataset/test-tweets-given.txt"
verbose = False

loader = ld(trainingFile, testingFile, verbose)
trainer = Trainer(0, 3, 0.1)
loader.resetLineCursor()

line = loader.getNextLineInTrainingData()
while (line != None):
    # print(line)
    trainer.feedLineInfo(line[2], line[3])
    line = loader.getNextLineInTrainingData()

# line = loader.getNextLineInTrainingData()
print(trainer.euTab.table, 'eu')
print(trainer.caTab.table, 'ca')
print(trainer.glTab.table, 'gl')
print(trainer.esTab.table, 'es')
print(trainer.enTab.table, 'en')
print(trainer.ptTab.table, 'pt')
# while(line != None):
#     trainer.feedLineInfo(line[2], line[3])
#     line = loader.getNextLineInTrainingData()


# print(trainer.tab.table)

# print(trainer.euTab.table)
# print(trainer.caTab.table)
# print(trainer.glTab.table)
# print(trainer.esTab.table)
# print(trainer.enTab.table)
# print(trainer.ptTab.table)

# print(math.log10(10))
