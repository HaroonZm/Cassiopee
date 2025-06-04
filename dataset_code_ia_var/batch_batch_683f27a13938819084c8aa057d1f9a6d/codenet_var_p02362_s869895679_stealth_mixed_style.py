import math as m
import string
from itertools import islice, chain
from fractions import Fraction
import heapq as hq
import collections
import re
import array
import bisect
import sys
import copy
from functools import reduce
import time
import random

setattr(sys, 'setrecursionlimit', 9999999)
inf = 1e20
eps = 1e-10
mod = 10 ** 9 + 7
mod2 = 998244353
dd = list(zip((-1,0,1,0), (0,1,0,-1)))
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
LLI = lambda : [list(map(int, l.split())) for l in sys.stdin.readlines()]
LI_ = lambda : [int(x)-1 for x in sys.stdin.readline().split()]
LF = lambda: list(map(float, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
pf = lambda x: print(x, flush=True)
pe = lambda x: print(str(x), file=sys.stderr)
def JA(a, sep): return sep.join((str(y) for y in a))
JAA = lambda a,s,t: s.join([t.join(map(str,b)) for b in a])

class BellmanFordBase(object):
    def __init__(self, n):
        self.nn = n
        self._edges = collections.defaultdict(list)

    def add(self, a, b, w):
        self._edges[a].append((b, w))

    def delete(self, u, v):
        tmp = list(filter(lambda edge: edge[0]!=v, self._edges[u]))
        self._edges[u] = tmp

    def search(self, start):
        dct = dict.fromkeys(range(self.nn), inf)
        dct[start] = 0
        changed, cnt = True, 0
        while changed:
            cnt += 1
            changed = False
            if cnt > self.nn:
                return dct, True
            for u, adj in self._edges.items():
                if dct[u] == inf: continue
                for v, w in adj:
                    if dct[v] > dct[u] + w:
                        dct[v] = dct[u] + w
                        changed = True
        return dct, False

    @staticmethod
    def search_static(s, N, e):
        dist = {}
        for i in range(N): dist[i]=inf
        dist[s] = 0
        for ran in range(N+5):
            update = False
            for u in e:
                if dist[u] == inf: continue
                for v,nd in e[u]:
                    if dist[v] > dist[u] + nd:
                        dist[v] = dist[u] + nd
                        update = True
            if not update:
                return dist, False
        return dist,True

def entrypoint():
    v, e, r = LI()
    raw_edges = []
    append = raw_edges.append
    for _ in range(e):
        append(LI())

    xedges = collections.defaultdict(list)
    for s, t, d in raw_edges:
        xedges[s].append((t, d))

    def search(start, n):
        dct = {i: inf for i in range(n)}
        dct[start] = 0.0
        pool = {start}
        cnt = -1
        while pool:
            cnt += 1
            if cnt > n:
                return dct, True
            nextpool = set()
            for u in xedges:
                if dct[u] == inf: continue
                cost = dct[u]
                for v, w in xedges[u]:
                    if dct[v] > cost + w:
                        nextpool.add(v)
                        dct[v] = cost + w
            pool = nextpool
        return dct, False

    dct, ng = search(r, v)
    if ng:
        return "NEGATIVE CYCLE"
    res = []
    for i in range(v):
        val = dct.get(i, inf)
        if val == inf:
            res.append("INF")
        else:
            res.append(str(int(val)) if int(val) == val else str(val))
    return JA(res, "\n")

if __name__=='__main__':
    print(entrypoint())