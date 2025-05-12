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
    n = I()
    li = list("ixcm")
    k = [1,10,100,1000]
    d = {"i":1,"x":10,"c":100,"m":1000}
    f = ["i","x","c","m"]
    for _ in range(n):
        a,b = LS()
        s = 0
        for i in range(len(a)):
            if a[i] in li:
                a[i] = d[a[i]]
                if i > 0 and a[i-1] not in k:
                    s += a[i-1]*a[i]
                else:
                    s += a[i]
            else:
                a[i] = int(a[i])

        for i in range(len(b)):
            if b[i] in li:
                b[i] = d[b[i]]
                if i > 0 and b[i-1] not in k:
                    s += b[i-1]*b[i]
                else:
                    s += b[i]

            else:
                b[i] = int(b[i])
        ans = []
        while s != 0:
            i = int(math.log(s+0.1,10))
            m = s//k[i]
            s %= k[i]
            if m != 1:
                ans.append(m)
            ans.append(f[i])
        for i in ans:
            print(i,end="")
        print()
    return

#B
def B():
    d = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1)]
    while 1:
        t,n = LI()
        if t == n == 0:
            break
        f = defaultdict(lambda : 1)
        for i in range(n):
            x,y = LI()
            f[(x,y)] = 0
        x,y = LI()
        bfs = defaultdict(lambda : 1)
        q = deque()
        q.append((x,y,0))
        bfs[(x,y)] = 0
        ans = 1
        while q:
            x,y,turn = q.popleft()
            if turn < t:
                for dx,dy in d:
                    x2 = x+dx
                    y2 = y+dy
                    if bfs[(x2,y2)]:
                        if f[(x2,y2)]:
                            ans += 1
                            bfs[(x2,y2)] = 0
                            q.append((x2,y2,turn+1))
        print(ans)
    return

#C
def C():
    return

#D
def D():
    def f(n):
        if d[n] != None:
            return d[n]
        else:
            i = int(math.log(n+0.1,10))
            d[n] = d[10**i]
            m = n-10**i
            d[n] += (i+1)*m
            return d[n]
    lis = [1]
    for i in range(10):
        lis.append(lis[-1]+(i+1)*9*10**i)
    d = defaultdict(lambda : None)
    for i in range(11):
        d[10**i] = lis[i]

    while 1:
        n,k = LI()
        if n == k == 0:
            break
        l = 0
        r = 1000000000
        while r-l > 1:
            m = (r+l)//2
            if n < f(m):
                r = m
            else:
                l = m
        s = str(l)[n-f(l):]
        n = l
        while len(s) <= k:
            k -= len(s)
            print(s,end="")
            n += 1
            s = str(n)
        print(s[:k])
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