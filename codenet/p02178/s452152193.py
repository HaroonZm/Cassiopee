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
    n,t,s,e = LI()
    s -= 1
    e -= 1
    v = [[] for i in range(n)]
    f = [0]*n
    for i in range(n-1):
        a,b,w = LI()
        a -= 1
        b -= 1
        v[a].append((b,w))
        v[b].append((a,w))
        f[a] += 1
        f[b] += 1

    bfs = [1]*n
    bfs[s] = 0
    q = deque([s])
    par = [None]*n
    while q:
        x = q.popleft()
        for y,w in v[x]:
            if bfs[y]:
                par[y] = [x,w-t*(f[x]-1)]
                bfs[y] = 0
                q.append(y)
    path = [0]*n
    while e != s:
        path[e] = 1
        e = par[e][0]
    bfs = [1]*n
    bfs[s] = 0
    q = deque([s])
    child = [[] for i in range(n)]
    while q:
        x = q.popleft()
        for y,w in v[x]:
            if bfs[y]:
                if not path[y]:
                    child[x].append(w-t*(f[y]-1))
                bfs[y] = 0
                q.append(y)
    for x in range(n):
        if path[x]:
            if par[x][1] <= 0:
                print("No")
                return
        child[x].sort()
        for i in range(len(child[x])):
            child[x][i] -= t*(i+1)
            if child[x][i] <= 0:
                print("No")
                return
    print("Yes")
    return

if __name__ == "__main__":
    solve()