#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
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
    from itertools import permutations
    def dot(a,b):
        return sum(list(map(lambda x : x[0]*x[1], zip(a,b))))

    n = I()
    p = LIR(n)
    ans = float("inf")
    for l in permutations(range(n),n):
        x,y = [0,0]
        m = 0
        v = [1,0]
        for i in l:
            s,t = p[i]
            nv = [s-x,t-y]
            m += math.acos(dot(v,nv)/(dot(v,v)*dot(nv,nv))**0.5)
            x,y = s,t
            v = [nv[0],nv[1]]
        s,t = 0,0
        nv = [s-x,t-y]
        m += math.acos(dot(v,nv)/(dot(v,v)*dot(nv,nv))**0.5)
        ans = min(ans, m)
    print(ans*180/math.pi)
    return

if __name__ == "__main__":
    solve()