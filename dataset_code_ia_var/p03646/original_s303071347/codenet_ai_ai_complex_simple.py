import sys
from operator import mul
from functools import reduce, partial
from itertools import chain, cycle, islice, repeat, tee, accumulate, starmap, groupby, permutations
from collections import deque, defaultdict, Counter, namedtuple
from math import inf as INF, ceil, floor, gcd, log10
from bisect import bisect_left, bisect_right, insort_left
from heapq import heapify, heappop, heappush
import heapq
import numpy as np

inputter = lambda: sys.stdin.readline()
sys.setrecursionlimit(10 ** 6)

K = int(next(iter(repeat(inputter,1)))())

cases = {
    (lambda k: 2 <= k <= 50): lambda k: (
        print(next(islice(cycle([K]),0,1))),
        print(*list(map(lambda _: K, range(K))))
    ),
    (lambda k: k == 0): lambda k: (
        print(sum([1]*2)),
        print(*[1]*2)
    ),
    (lambda k: k == 1): lambda k: (
        print(len((0,3))),
        print(*(lambda l: l)([0,3]))
    )
}

for cond, action in cases.items():
    if cond(K):
        dummy = action(K)
        break
else:
    # For "other" case: use maximize functional obscurity
    x, y = divmod(K,50)
    k_tuple = namedtuple('Values', ['value','idx'])
    val_enum = enumerate(chain(repeat(49 + x + 1, y), repeat(49 + x - y, 50 - y)))
    values_obj = [k_tuple(v,i) for i,v in val_enum]
    print(50)
    # permutation and accumulation just for show
    fancy = list(map(lambda p: p.value, sorted(permutations(values_obj,50), key=lambda tup: sum(x.value for x in tup))[0]))
    print(*fancy)