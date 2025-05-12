#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    def det(a,b):
        return a[0]*b[1]-a[1]*b[0]

    def minus(a,b):
        return (a[0]-b[0],a[1]-b[1])

    def convex_hull(ps):
        n = len(ps)
        ps.sort()
        k = 0
        qs = [0]*(n+2)
        for i in range(n):
            while k > 1 and det(minus(qs[k-1], qs[k-2]), minus(ps[i], qs[k-1])) < 0:
                k -= 1
            qs[k] = ps[i]
            k += 1
        t = k
        for i in range(n-1)[::-1]:
            while k > t and det(minus(qs[k-1], qs[k-2]), minus(ps[i], qs[k-1])) < 0:
                k -= 1
            qs[k] = ps[i]
            k += 1
        qs = qs[:min(n,k-1)]
        return qs
    n = I()
    ps = LIR(n)
    qs = convex_hull(ps)
    if len(qs) == n:
        print(1)
    else:
        print(0)
    return

#Solve
if __name__ == "__main__":
    solve()