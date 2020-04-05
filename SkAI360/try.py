import math
import string
import locale
from vocabularyvalidator import VocabularyValidator as vv
from ngram import NGram
from loader import Loader as ld
from trainer import Trainer
from tester import Tester
from writer import Writer

# init PARAMs
verbose = False
extra = [0, 1]
# demo PARAMs
# demoParam = [[0, 1, 0], [1, 2, 0.5], [1, 3, 1], [2, 2, 0.3]]
demoParam = []
demoParam.append([2, 2, 0.1])
demoParam.append([2, 2, 0.01])
demoParam.append([2, 2, 0.001])
demoParam.append([2, 3, 0.1])
demoParam.append([2, 3, 0.01])
demoParam.append([2, 3, 0.001])

# main execute loop
for param in demoParam:
    for e in extra:
        print('vocabulary =', param[0], 'ngram =', param[1],
              'delta =', param[2], 'extra =', e)
        loader = ld(verbose)
        trainer = Trainer(param[0], param[1], param[2], verbose, e)
        loader.resetLineCursor()

        line = loader.getNextLineInTrainingData()

        while (line != None):
            trainer.feedLineInfo(line[2], line[3])
            line = loader.getNextLineInTrainingData()

        # trainer.fillRestTable()

        tester = Tester(trainer)
        loader.resetLineCursor()
        line = loader.getNextLineInTestingData()

        while(line != None):
            tester.doTestLine(line, loader.getLineCursorPos())
            line = loader.getNextLineInTestingData()

        print(tester.getAccuracy())

        tester.dumpResult()
