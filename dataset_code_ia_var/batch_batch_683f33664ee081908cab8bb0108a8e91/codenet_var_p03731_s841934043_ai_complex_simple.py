from functools import reduce
from itertools import tee, islice, chain

N, T = map(int,input().split())
trr = list(map(int,input().split()))

def calculate(n, t, times):
    pair_prev, pair_curr = tee(times)
    pair_prev = chain([None], pair_prev)
    zipped = zip(pair_prev, pair_curr)
    def reducer(acc, elems):
        prev, curr = elems
        if prev is None:
            return acc + t
        overlap = max(0, prev + t - curr)
        return acc + t - overlap
    return reduce(reducer, zipped, 0)

print(calculate(N, T, trr))