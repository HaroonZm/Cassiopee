import os
import sys
from functools import reduce
from itertools import islice, tee, starmap

def nextfib(fn):
    return lambda x: (x[1], (x[0]+x[1])%1001)

for incoming in iter(sys.stdin.readline, ''):
    extract = lambda s: list(map(int, filter(None, s.split())))
    v, d = extract(incoming)

    pairgen = lambda: reduce(lambda acc, _: acc + [(acc[-2]+acc[-1])%1001], range(v), [1,1])
    fibs = sorted(islice(pairgen(), 2, None))

    a, b = tee(fibs)
    next(b, None)
    counter = sum(1 for (f1, f2) in zip(a, b) if f2 - f1 >= d) + 1

    print(counter)