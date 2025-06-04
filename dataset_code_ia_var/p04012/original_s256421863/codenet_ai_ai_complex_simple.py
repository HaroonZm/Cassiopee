from functools import reduce
from collections import Counter
from itertools import chain, groupby
import operator
w = input()
c = Counter(w)
lens = list(map(lambda x: x[1], sorted(c.items(), key=lambda y: y[0])))
evens = all(map(lambda x: x % 2 == 0, lens))
print(['No', 'Yes'][len(w) % 2 == 0 and evens])