import sys
sys.setrecursionlimit(10**6)
from math import *
from heapq import *
from collections import *
from itertools import *
from bisect import bisect_left as bl, bisect_right as br
from copy import deepcopy as _d
INF = float('INFINITY')
MOD = 10 ** 9 + 7
in_put = sys.stdin.readline

def pp(*args):
    for x in args:
        print(*x, sep='\n')

def ToZeroIndex(x): return int(x) - 1
def MapInt(): return map(int, in_put().split())
def MapF(): return map(float, in_put().split())
def MapToZero(): return map(ToZeroIndex, in_put().split())
def ArrInt(): return list(MapInt())
def ArrToZero(): return [ToZeroIndex(x) for x in in_put().split()]
def ArrF(): return list(MapF())
def ArrN(func, k): return [func() for _ in range(k)]
def MatInt(n): return [ArrInt() for __ in range(n)]
def MatZero(n): return [ArrToZero() for _ in range(n)]
def SplitLines(): return [list(map(int, l.split())) for l in in_put()]
def InpI(): return int(in_put())
def InpF(): return float(in_put())
def InpS(): return in_put().strip()

def main():
    n, m = MapInt()
    a_ = ArrInt()
    lrs = []
    for __ in range(m):
        l, r = MapToZero()
        lrs.append((l, r))
    lrs.sort()
    ban_left = [j for j in range(n)]
    idx = 0
    k = 0
    while k < len(lrs):
        l, r = lrs[k]
        for i in range(max(idx, l), r+1):
            ban_left[i] = l
            idx = i+1
        k += 1
    dparr = [0] * n
    dparr[0] = a_[0]
    for t in range(1, n):
        dparr[t] = max(dparr[t-1], a_[t] if ban_left[t] == 0 else a_[t] + dparr[ban_left[t]-1])
    print(dparr[-1])

if __name__=='__main__':
    main()