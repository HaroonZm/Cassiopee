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

move = [(0,1),(1,0)]
def solve(n):
    f = defaultdict(lambda : 0)
    v = defaultdict(list)
    l = []
    for i in range(n):
        a,b,dir = input().split()
        a = int(a)
        b = int(b)
        f[(a,b)] = 1
        dir = 0 if dir == "x" else 1
        na,nb = a+1-dir,b+dir
        f[(na,nb)] = 1
        l.append((a,b,na,nb))
        l.append((na,nb,a,b))
        v[(a,b)].append(((na,nb),1))
        v[(na,nb)].append(((a,b),1))
    for a,b,c,d in l:
        for dx,dy in move:
            na,nb = a+dx,b+dy
            if f[(na,nb)] and (c,d) != (na,nb):
                v[(a,b)].append(((na,nb),0))
                v[(na,nb)].append(((a,b),0))
    bfs = defaultdict(lambda : -1)
    q = deque()
    for a,b,c,d in l:
        if bfs[(a,b)] < 0:
            q.append((a,b))
            bfs[(a,b)] = 0
            while q:
                x,y = q.popleft()
                for node,k in v[(x,y)]:
                    nx,ny = node
                    if k:
                        nb = 1-bfs[(x,y)]
                    else:
                        nb = bfs[(x,y)]
                    if bfs[(nx,ny)] >= 0:
                        if bfs[(nx,ny)] != nb:
                            print("No")
                            return
                    else:
                        bfs[(nx,ny)] = nb
                        q.append((nx,ny))
    print("Yes")
    return

#Solve
if __name__ == "__main__":
    while 1:
        n = I()
        if n == 0:
            break
        solve(n)