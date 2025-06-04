import math
import string
from itertools import *
import fractions
import heapq as hq
import collections
import re
from array import array
import bisect as bsc
import sys
from copy import deepcopy as dc
import functools
import time
import random as rnd

setattr(sys, 'setrecursionlimit', int(1e7))
INF, EPS = 10 ** 20, 1.0 / 10 ** 10
MOD = int(1e9 + 7)
MOD2 = 998244353
nn = [(-1,0), (0,1), (1,0), (0,-1)]
n8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

LI = lambda: list(map(int, sys.stdin.readline().split()))
LLI = lambda: [list(map(int, line.split())) for line in sys.stdin.readlines()]
def LI_(): return [int(z)-1 for z in sys.stdin.readline().split()]
LF = lambda: [float(i) for i in sys.stdin.readline().split()]
LS = lambda: sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
S = input
pf = lambda s: print(s, flush=True)
def pe(x): print(str(x), file=sys.stderr)
def JA(arr, sp): return sp.join(str(i) for i in arr)
def JAA(mat, sp1, sp2): return sp1.join(sp2.join(str(b) for b in a) for a in mat)

class RangeAddSum(object):
    def __init__(yo, n):
        l = 1
        while (2 << (l-1)) <= n: l += 1
        yo.N = 1 << l
        yo.A = [0] * (yo.N*2)
        yo.B = [0] * (yo.N*2)
    def add(self, a, b, x, k, l, r):
        def plus(K, L, R):
            if a <= L and R <= b:
                self.A[K] += x
            elif L < b and a < R:
                self.B[K] += (min(b, R)-max(a, L))*x
                M = (L+R)//2
                plus(K*2+1, L, M)
                plus(K*2+2, M, R)
        plus(k, l, r)
    def query(me, a, b, k, l, r):
        def q(K, L, R):
            if b <= L or R <= a: return 0
            if a <= L and R <= b: return me.A[K]*(R-L) + me.B[K]
            rs = (min(b, R)-max(a, L))*me.A[K]
            M = (L+R)//2
            rs += q(K*2+1, L, M)
            rs += q(K*2+2, M, R)
            return rs
        return q(k, l, r)

def main():
    n, q = LI()
    dat = []
    for _ in range(q):
        dat.append(LI())
    addsum = RangeAddSum(n)
    out = []
    for qq in dat:
        s = qq[1] - 1
        t = qq[2]
        if qq[0] == 0:
            addsum.add(s, t, qq[3], 0, 0, n)
        else:
            out.append(addsum.query(s, t, 0, 0, n))
    return JA(out, '\n')

print(main())