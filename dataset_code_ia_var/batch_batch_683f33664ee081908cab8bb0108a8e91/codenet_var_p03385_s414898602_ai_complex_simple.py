from collections import Counter
from functools import reduce
from operator import eq

s = input()
c = Counter(s)
verdict = {True: 'Yes', False: 'No'}[
    reduce(lambda x, y: x and y, (eq(c[l],1) for l in 'abc')) and len(c)==3
]
print(verdict)