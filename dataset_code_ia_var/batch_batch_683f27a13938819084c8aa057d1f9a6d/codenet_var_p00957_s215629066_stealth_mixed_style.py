import sys
from collections import deque
from decimal import Decimal
import itertools as IT

sys.setrecursionlimit(10**6)

inf = float('inf')
modulo = 1000000007

def get_input():
    l, k = map(int, raw_input().split())
    return l, k

def weird_prog_mix():
    l, k = get_input()

    X = [0 for _ in range(201)]
    x2 = [1] + [0]*200

    # procedural loop with imperative style
    for idx in range(1, l+1):
        X[idx] = x2[idx-1]
        x2[idx] = X[idx-1]
        # functional touch
        if idx >= k:
            X[idx] = (lambda a, b: a + b)(X[idx], x2[idx - k])
    
    def fold(fun, seq):
        # simulate functional reduce, even though could use functools.reduce
        res = 0
        for el in seq:
            res = fun(res, el)
        return res

    # comprehension + folding
    print fold(lambda a, b: a+b, (X[j] for j in range(len(X))))

weird_prog_mix()