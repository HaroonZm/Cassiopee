import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
mod2 = 998244353
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)

class BellmanFord:
    def __init__(self, n):
        self.N = n
        self.e = collections.defaultdict(list)

    def add(self, u, v, d):
        self.e[u].append((v,d))

    def delete(self, u, v):
        self.e[u] = [_ for _ in self.e[u] if _[0] != v]

    def search(self, s):
        d = collections.defaultdict(lambda: inf)
        d[s] = 0
        update = True
        cnt = 0
        while update:
            cnt += 1
            if cnt > self.N:
                return d,True
            update = False
            for k,v in self.e.items():
                if d[k] == inf:
                    continue
                dk = d[k]
                for n,nd in v:
                    if d[n] > dk + nd:
                        update = True
                        d[n] = dk + nd

        return d,False

    # 繝｡繧ｽ繝・ラ縺ｮ縺ｿ迚・
    def search(s, N):
        d = collections.defaultdict(lambda: inf)
        d[s] = 0
        update = True
        cnt = 0
        while update:
            cnt += 1
            if cnt > N:
                return d,True
            update = False
            for k,v in e.items():
                if d[k] == inf:
                    continue
                dk = d[k]
                for n,nd in v:
                    if d[n] > dk + nd:
                        update = True
                        d[n] = dk + nd

        return d,False

def main():
    v,e,r = LI()
    std = [LI() for _ in range(e)]

    e = collections.defaultdict(list)
    for s,t,d in std:
        e[s].append((t,d))

    def search(s, N):
        d = collections.defaultdict(lambda: inf)
        d[s] = 0
        us = set([s])
        cnt = 0
        while us:
            cnt += 1
            if cnt > N:
                return d,True
            ns = set()
            for k,v in e.items():
                if d[k] == inf:
                    continue
                dk = d[k]
                for n,nd in v:
                    if d[n] > dk + nd:
                        ns.add(n)
                        d[n] = dk + nd
            us = ns

        return d,False

    d,f = search(r,v)
    if f:
        return "NEGATIVE CYCLE"

    r = []
    for i in range(v):
        t = d[i]
        if t == inf:
            r.append("INF")
        else:
            r.append(t)

    return JA(r, "\n")

print(main())