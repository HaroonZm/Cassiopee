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
def S(): return list(sys.stdin.readline())[:-1]
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
    n,m = LI()
    e = []
    f = [[0]*n for i in range(n)]
    v = [[] for i in range(n)]
    for i in range(m):
        a,b,c = LI()
        a -= 1
        b -= 1
        e.append([a,b,c])
        f[a][b] = c
        f[b][a] = c
        v[a].append(b)
        v[b].append(a)
    ans = 0
    S = []
    for p in range(n):
        K = [{p}]
        for q in v[p]:
            K += [s|{q} for s in K]
        S += K
    for s in S:
        for x in s:
            for y in s:
                if x == y:
                    continue
                if f[x][y] > 0:
                    continue
                else:
                    break
            else:
                continue
            break
        else:
            m = [float("inf")]*n
            for a in s:
                for b in s:
                    if a == b:
                        continue
                    if f[a][b] < m[a]:
                        m[a] = f[a][b]
                    if f[a][b] < m[b]:
                        m[b] = f[a][b]
            k = 0
            for i in m:
                if i != float("inf"):
                    k += i
            if ans < k:
                ans = k

    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()