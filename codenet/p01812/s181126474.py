import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

def main():
    n,m,k = LI()
    d = LI_()
    v = [LI_() for _ in range(n)]
    dd = collections.defaultdict(lambda: None)
    for i in range(m):
        dd[d[i]] = i
    ii = [2**_ for _ in range(m)]
    vv = [[ii[dd[v[c][i]]] if not dd[v[c][i]] is None else 0  for c in d] for i in range(k)]
    m2 = 2**m
    u = [None] * m2
    u[-1] = 1
    q = [m2-1]
    r = 0
    while q:
        r += 1
        nq = []
        for qd in q:
            qdi = [di for di in range(m) if qd & ii[di]]
            for vi in range(k):
                t = 0
                vvi = vv[vi]
                for di in qdi:
                    t |= vvi[di]
                if not u[t] is None:
                    continue
                if t == 0:
                    return r
                u[t] = 1
                nq.append(t)
        q = nq

    return -1

print(main())