from functools import reduce
from operator import add

from itertools import islice, tee, chain, starmap

def flat(t):
    return [item for sublist in t for item in sublist]

def splat(f):
    return lambda args: f(*args)

class Sentinel(Exception): pass

def infinite_input():
    try:
        while True:
            yield input()
    except EOFError:
        return

def chunker(it, size):
    its = tee(it, size)
    for idx, t in enumerate(its):
        for _ in range(idx):
            next(t, None)
    return zip(*its)

def overcomplicated():
    input_stream = iter(infinite_input())
    try:
        while True:
            n = int(next(input_stream))
            if n == 0:
                raise Sentinel()
            data = ([int(x) for x in next(input_stream).split()] for _ in range(n))
            process = lambda d: (
                reduce(add, islice(d,1,9,2))*60 + reduce(add, islice(d,2,10,2)),
                d[0]
            )
            pairs = list(map(process, data))
            indices = list(starmap(lambda *_: _[-1], sorted(pairs)))
            print(indices[0])
            print(indices[1])
            print(indices[-2])
    except Sentinel:
        pass

overcomplicated()