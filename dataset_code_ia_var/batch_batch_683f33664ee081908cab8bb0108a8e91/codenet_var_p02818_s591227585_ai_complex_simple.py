import sys, math, functools, operator
def input(): return sys.stdin.readline()[:-1]
from itertools import islice, accumulate, chain, product, permutations, combinations, cycle
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10**7)

A, B, K = map(int, input().split())

out = list(
    islice(
        (
            (lambda a, b, k: (a - k, b) if k <= a else (0, max(0, b - (k - a))))(a, b, k)
            for a, b, k in [ (A, B, K) ]
        ),
        1
    )
)[0]

print(*out)