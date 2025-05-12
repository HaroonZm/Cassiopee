#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS():return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = I()
    return l
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LI()
    return l
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = S()
    return l
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LS()
    return l
sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    while 1:
        n = I()
        if n == 0:
            quit()
        a = LI()
        m = sum(a)/n
        c = 0
        for i in range(n):
            if a[i] <= m:
                c += 1
        print(c)
    return

#B
def B():
    while 1:
        n = I()
        if n == 0:
            quit()
        t = [0 for i in range(24*3600)]
        for i in range(n):
            x,y = input().split()
            x = list(map(int, x.split(":")))
            y = list(map(int, y.split(":")))
            l = x[0]*3600+x[1]*60+x[2]
            r = y[0]*3600+y[1]*60+y[2]
            t[l] += 1
            t[r] -= 1
        ans = 0
        for i in range(24*3600-1):
            t[i+1] += t[i]
            ans = max(ans, t[i])
        print(ans)
    return
#C
def C():
    n = I()
    if n == 0:
        print(1)
    elif n == 1:
        print(2)
    elif n == 2:
        print(1)
    else:
        print(0)
    return

#D
def D():
    def dijkstra(s):
        d = [float("inf") for i in range(n)]
        q = [[0,s]]
        d[s] = 0
        while q:
            dx,x = heappop(q)
            for y in v[x]:
                if dx+1 < d[y]:
                    d[y] = d[x]+1
                    heappush(q,[d[y],y])
        return d
    n,m,s,t = LI()
    s -= 1
    t -= 1
    v = [[] for i in range(n)]
    for i in range(m):
        x,y = LI()
        x -= 1
        y -= 1
        v[x].append(y)
        v[y].append(x)
    l = dijkstra(s)
    l2 = dijkstra(t)
    k = l[t]-2
    d = defaultdict(int)
    ans = 0
    for i in l2:
        d[i] += 1
    for i in l:
        ans += d[max(-1,k-i)]
    print(ans)
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#I
def I_():
    return

#J
def J():
    return

#Solve
if __name__ == "__main__":
    D()