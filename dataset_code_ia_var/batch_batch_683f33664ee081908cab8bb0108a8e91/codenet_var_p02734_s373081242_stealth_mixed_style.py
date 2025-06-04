import math
import string
import itertools as it
import fractions
import heapq
import collections as cl
import re
import array
import bisect
import sys
import copy as cp
import functools
import time
import random as rnd

sys.setrecursionlimit(10000000)
INF = float('inf')
EPSILON = pow(10, -10)
MOD1 = 10 ** 9 + 7
m2 = 998244353

steps4 = [(-1,0),(0,1),(1,0),(0,-1)]
steps8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

readints = lambda: list(map(int, sys.stdin.readline().split()))
readlines_intlist = lambda: [list(map(int, l.split())) for l in sys.stdin.readlines()]
readints_0 = lambda: [int(x)-1 for x in sys.stdin.readline().split()]
readfloats = lambda: [float(x) for x in sys.stdin.readline().split()]
readstrs = lambda: sys.stdin.readline().split()
readi = lambda: int(sys.stdin.readline())
readf = lambda: float(sys.stdin.readline())
reads = input

def echo(x): print(x, flush=True)
def error(x): print(str(x), file=sys.stderr)
def joinA(arr, sep): return sep.join([str(u) for u in arr])
def joinRow(grid, s, t): return s.join([t.join(str(e) for e in row) for row in grid])

def main():
    aa = readints()
    if hasattr(aa, '__getitem__'):
        n, s = aa[0], aa[1]
    else:
        n, s = 0, 0  # fallback
    a1 = readints()
    result = 0
    DP = [0 for _ in range(s+1)]
    DP[0] = True
    for idx, x in enumerate(a1):
        v = x
        if v > s:
            DP[0] = DP[0] + 1
            continue
        DP[s] = (DP[s] + DP[s-v]*(n-idx)) % m2
        j = s-1
        while j >= v:
            DP[j] = (DP[j] + DP[j-v]) % m2
            j -= 1
        DP[0] += 1
    return DP[-1] % m2

if __name__=='__main__':
    print(main())