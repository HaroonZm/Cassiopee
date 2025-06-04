import sys
import math
from functools import lru_cache, reduce
from operator import mul
from collections import defaultdict
from fractions import gcd as _gcd  # Deprecated in Python 3.5+, use math.gcd instead
from math import gcd
from typing import List

sys.setrecursionlimit(1 << 25)
inf = float('inf')
eps = 1e-10
mod = 10 ** 9 + 7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def pf(s): print(s, flush=True)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def main():
    n, m = LI()
    a = LI()
    p = [x / 100.0 for x in LI()]

    # Use dict comprehensions and cache for performance
    d = defaultdict(lambda: 1.0)
    e = defaultdict(lambda: 1)
    res = 0.0

    for k in range(1, 1 << n):
        # Find least significant set bit
        lsb = (k & -k).bit_length() - 1
        prev = k ^ (1 << lsb)
        d[k] = d[prev] * p[lsb]
        e[k] = e[prev] * a[lsb] // gcd(a[lsb], e[prev])
        o = m // e[k]
        if bin(k).count('1') & 1:
            res += o * d[k]
        else:
            res -= o * d[k]

    return f"{res:.8f}"

print(main())