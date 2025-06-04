import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

n,m,k = [int(x) for x in sys.stdin.readline().split()]
d = [int(x)-1 for x in sys.stdin.readline().split()]
v = []
for _ in range(n):
    v.append([int(x)-1 for x in sys.stdin.readline().split()])

dmap = collections.defaultdict(lambda: None)
for i in range(m):
    dmap[d[i]] = i
ii = []
for _ in range(m):
    ii.append(2 ** _)

vv = []
for i in range(k):
    tmp = []
    for c in d:
        idx = dmap[v[c][i]]
        if idx is not None:
            tmp.append(ii[idx])
        else:
            tmp.append(0)
    vv.append(tmp)

m2 = 2 ** m
u = [None] * m2
u[-1] = 1
q = [m2 - 1]
r = 0
found = False
while q and not found:
    r += 1
    nq = []
    for qd in q:
        qdi = []
        for di in range(m):
            if qd & ii[di]:
                qdi.append(di)
        for vi in range(k):
            t = 0
            vvi = vv[vi]
            for di in qdi:
                t |= vvi[di]
            if u[t] is not None:
                continue
            if t == 0:
                print(r)
                found = True
                break
            u[t] = 1
            nq.append(t)
        if found:
            break
    q = nq
if not found:
    print(-1)