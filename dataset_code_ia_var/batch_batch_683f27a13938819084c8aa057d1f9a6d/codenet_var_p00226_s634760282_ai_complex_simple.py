from functools import reduce
from itertools import starmap, repeat, count
from operator import eq

def extravagant():
    _input = iter(lambda: input().split(), ['0'])
    for r, a in _input:
        hit = sum(starmap(eq, zip(r, a)))
        blow = (lambda t: sum(map(lambda c: min(r.count(c), a.count(c)), set(r))) - hit)(tuple())
        print(hit, blow)
extravagant()