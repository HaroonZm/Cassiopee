import itertools
import operator

S = input()
options = dict(itertools.zip_longest(['ABC','ARC'], ['ARC','ABC']))
print(operator.methodcaller('__getitem__', S)(options))