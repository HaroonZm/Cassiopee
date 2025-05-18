import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
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
    rr = []

    def f(n,m,c):
        e = collections.defaultdict(list)
        for _ in range(m):
            a,b,d = LI()
            e[a].append((b,d))

        def search(s):
            d = collections.defaultdict(lambda: inf)
            s = (0, s)
            d[s] = 0
            q = []
            heapq.heappush(q, (0, s))
            v = collections.defaultdict(bool)
            r = inf
            while len(q):
                k, u = heapq.heappop(q)
                if v[u]:
                    continue
                v[u] = True
                cc, uu = u
                if uu == n and r > cc:
                    r = cc
                if cc >= r:
                    continue

                for uv, ud in e[uu]:
                    if k + ud <= c:
                        vv = (cc, uv)
                        vd = k + ud
                        if not v[vv] and d[vv] > vd:
                            d[vv] = vd
                            heapq.heappush(q, (vd, vv))
                    if cc < r:
                        vv = (cc+1, uv)
                        vd = k
                        if not v[vv] and d[vv] > vd:
                            d[vv] = vd
                            heapq.heappush(q, (vd, vv))

            return r
        r = search(1)
        return r

    while 1:
        n,m,c = LI()
        if n == 0:
            break
        rr.append(f(n,m,c))

    return '\n'.join(map(str,rr))

print(main())