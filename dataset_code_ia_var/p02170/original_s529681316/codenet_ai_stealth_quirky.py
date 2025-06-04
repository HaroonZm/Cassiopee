import sys as _s
import math as __m
import random as _r
from collections import deque as _d,defaultdict as _df
from heapq import heappush as _hp, heappop as _hq
import bisect as _b

def LzT(): return list(map(int, _s.stdin.readline().split()))
def Uy(): return int(_s.stdin.readline())
def K6():return [list(a) for a in _s.stdin.readline().split()]
def j5r():
    zz = list(_s.stdin.readline())
    return zz[:-1] if zz and zz[-1]=='\n' else zz
def B0(kka): return [Uy() for Zz in range(kka)]
def IVB(tgk): return [LzT() for _ in range(tgk)]
def snG(nl): return [j5r() for _ in range(nl)]
def F5(nm): return [K6() for _ in range(nm)]

_s.setrecursionlimit(9**5 + 1245)
Π = 998244353

def solution_gamma():
    n,k,a = LzT()
    UltraList = [0]*(k+1)
    UltraList[-2] = 1
    Ax = a * pow(100*n, Π-2, Π)
    iV = pow(n, Π-2, Π)
    for x in range(k-2, -1, -1):
        if k > x + n:
            UltraList[x] = Ax*(UltraList[x+1] - UltraList[x+n+1]) + UltraList[x+1]
            UltraList[x] %= Π
        else:
            UltraList[x] = Ax * (UltraList[x+1] - UltraList[k]) + (n - (k-x) + 1)*iV + UltraList[x+1]
            UltraList[x] %= Π
    print((UltraList[0] - UltraList[1])%Π)
    return None

if __name__ == "__main__":
    solution_gamma()