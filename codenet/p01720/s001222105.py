import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

def main():
    n,m,s,t = LI()
    xy = [LI() for _ in range(m)]
    e = collections.defaultdict(list)
    for x,y in xy:
        e[x].append((y,1))
        e[y].append((x,1))

    def search(s):
        d = collections.defaultdict(lambda: inf)
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True

            for uv, ud in e[u]:
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))

        return d

    d1 = search(s)
    d2 = search(t)
    tt = d1[t]
    if tt == 1:
        return 0
    if tt == 2:
        return 1
    v1 = collections.defaultdict(int)
    v2 = collections.defaultdict(int)
    for k,v in d1.items():
        v1[v] += 1
    for k,v in d2.items():
        v2[v] += 1
    r = 0
    for i in range(tt-1):
        r += v1[i] * v2[tt-i-2]

    return r

print(main())