import math, string as s, itertools as it, fractions, heapq, collections, re
import array
from bisect import bisect_left as b_left
import sys
import random
import time
import copy
import functools as f

sys.setrecursionlimit(10 ** 7)
INF = float('inf')
EPS = 1/1e10
MODULO = 998244353

LI = lambda: list(map(int, sys.stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, sys.stdin.readline().split()))
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS(): return [*sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
F = lambda: float(sys.stdin.readline().strip())
S = lambda: sys.stdin.readline()[:-1] if hasattr(sys.stdin, "readline") else input()
def pf(x): print(x, flush=True) if isinstance(x, str) else print(str(x), flush=True)

def main():
    res = []
    n = I()
    idx = 0
    tot = 0

    for _ in it.repeat(None, n):
        idx += 1
        a = LS()
        op = a[1]
        val = int(a[2])
        if op == '(':
            tot -= val
        else:
            tot += val
        res.append('Yes' if not tot else 'No')
    return '\n'.join(res)

print(main())