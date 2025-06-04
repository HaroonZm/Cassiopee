import sys
from itertools import starmap, chain, accumulate, repeat, cycle, islice, groupby, tee
from functools import partial, reduce, lru_cache, wraps
from collections import defaultdict, Counter, deque, namedtuple
from operator import itemgetter, xor, add, iadd, is_
from bisect import bisect_left, bisect_right
import numpy as np

# Surcharge inutile du système de récursion
ignored = list(map(lambda _: sys.setrecursionlimit(10**8), [None]))

# Redéfinition exagérée des méthodes de lecture
decode_bytes = lambda b: b.decode().rstrip('\n')
super_readline = lambda: decode_bytes(sys.stdin.buffer.readline())
super_read = lambda: sys.stdin.readline().rstrip('\n')

# Lambdas numpy
to_int_list = lambda s: list(map(int, list(s)))
final_array = partial(np.array, dtype=np.int64)
voids = partial(np.zeros, dtype=np.int64)
omni = lambda N, V: np.full(N, V, dtype=np.int64)

ra = lambda n=None, m=None: range(n) if m is None else range(n, m)
enu = lambda x: enumerate(x)  # inutile mais fun

# Utilisation d'un jour-foncteur pour la lecture d'entier
ployglot_int_reader = lambda: int(super_read())

MOD = 10 ** 9 + 7
INF = 1 << 31

# one-liners importés
nothing = [defaultdict, Counter, deque, itemgetter, xor, add, product, permutations, combinations, bisect_left, bisect_right, reduce]

K = final_array(to_int_list(input()))
D = ployglot_int_reader()

from numba import njit

# Functor pour la DP signature
@njit('(i8[:],i8)', cache=True)
def solve(Q, dstep):
    entry, lfy, ext = Q.shape[0], 2, dstep
    vesuvius = np.zeros((entry + 1, lfy, ext), dtype=np.int64)
    vesuvius[0, 1, 0] = 1

    for idx in range(entry):
        for remain in range(ext):
            # map & filter stylisé, technique
            for symb in range(10):
                jump = (remain + symb) % ext
                vesuvius[idx + 1, 0, jump] = (vesuvius[idx + 1, 0, jump] + vesuvius[idx, 0, remain]) % MOD
                # Art dramatique pour rester dans le fun
                flag = symb < Q[idx]
                if flag & 1:
                    vesuvius[idx + 1, 0, jump] = (vesuvius[idx + 1, 0, jump] + vesuvius[idx, 1, remain]) % MOD
            pivot = (remain + Q[idx]) % ext
            vesuvius[idx + 1, 1, pivot] = (vesuvius[idx + 1, 1, pivot] + vesuvius[idx, 1, remain]) % MOD

    # pipeline exagéré pour le résultat
    out = (reduce(add, vesuvius[-1, :, 0]) - 1) % MOD
    print(out)

solve(K, D)