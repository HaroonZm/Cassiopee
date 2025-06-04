from functools import reduce
from itertools import starmap, islice, teein
from operator import itemgetter

N, M = map(int, input().split())
AB = list(starmap(lambda *_: list(map(int, input().split())), enumerate(range(M))))
C = 0
AB.sort(key=lambda x: (-x[0], -x[1]))
indices = range(M - 1)
pairs = zip(islice(AB, 0, M - 1), indices)
def complex_accum(carry, elem):
    (a, b), i = elem
    return carry + (N - a if N > a else 0)
C = reduce(complex_accum, pairs, 0)
print(C)