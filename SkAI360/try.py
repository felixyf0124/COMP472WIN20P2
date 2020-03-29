from vocabularyvalidator import VocabularyValidator as vv 

vValidator = vv()

print(vValidator.verify('a?',0))
print(vValidator.verify('aA',0))
print(vValidator.verify('a_a',0))
print(vValidator.verify('_a/?',0))
print(vValidator.verify('a?',1))
print(vValidator.verify('a_a',1))
print(vValidator.verify('AazB',1))
print(vValidator.verify('a?',2))
print(vValidator.verify('a_a',2))
print(vValidator.verify('_a/?',2))
print('A2/'.lower())
