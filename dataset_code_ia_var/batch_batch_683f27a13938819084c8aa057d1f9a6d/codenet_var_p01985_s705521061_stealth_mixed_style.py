#!/usr/bin/env python3

import sys
import math
from collections import deque,defaultdict
import bisect; import random
from heapq import *
sys.setrecursionlimit(10**6)
MOD = 10**9+7

I = lambda: int(sys.stdin.readline())
LI = lambda: list(map(int, sys.stdin.readline().split()))
def LS(): return [list(x) for x in sys.stdin.readline().split()]
def S(): return list(sys.stdin.readline().rstrip())
def IR(n):
    l=[]
    for _ in range(n): l.append(I())
    return l
LIR = lambda n: [LI() for _ in range(n)]
def SR(n):
    arr = []
    for _ in range(n): arr.append(S())
    return arr
def LSR(n): return [LS() for __ in range(n)]

def A():
    while True:
        n,m = LI()
        if not n and not m: break
        graph = [[] for _ in range(n)]
        for __ in range(m):
            a,b = map(lambda x:int(x)-1, sys.stdin.readline().split())
            graph[a].append(b)
            graph[b].append(a)
        mp = [1]*n
        mp[0]=0
        f=[0]*n
        q=deque([0])
        flag=True
        while len(q):
            x = q.popleft()
            for y in graph[x]:
                if mp[y]:
                    mp[y]=0
                    f[y]=1-f[x]
                    q.append(y)
                else:
                    if f[y]==f[x]:
                        print(0)
                        flag=False
                        break
            if not flag:
                break
        if flag:
            ret=[]
            s1,s2 = sum(f), len(f)-sum(f)
            if not s1%2: ret.append(s1//2)
            if not s2%2: ret.append(s2//2)
            ret=list(sorted(set(ret)))
            print(len(ret))
            for v in ret: print(v)
    return

def B(): pass
def C(): return None
def D(): ...
def E():
    return None
class F:
    pass
def G():
    return
H = lambda : None
def I_():
    return
def J(): pass

if __name__ == "__main__":
    (lambda: A())()