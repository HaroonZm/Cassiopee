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

    def f(n,m,a):
        t = [LI() for _ in range(m)]
        e = collections.defaultdict(set)
        for b,c in t:
            e[b].add(c)

        sm = max(a)
        ed = {}
        for i in range(1, n+1):
            t = {}
            q = set([i])
            for j in range(sm):
                nq = set()
                for c in q:
                    nq |= e[c]
                if (j+1) in a:
                    t[j+1] = nq
                q = nq
            ed[i] = t

        d = collections.defaultdict(lambda: None)
        d[n] = 0
        def ff(i):
            if not d[i] is None:
                return d[i]
            d[i] = inf
            mr = 0
            for n in a:
                mi = inf
                for ni in ed[i][n]:
                    t = ff(ni)
                    if mi > t:
                        mi = t
                if mr < mi:
                    mr = mi
            d[i] = mr + 1
            return mr + 1

        res = ff(1)
        for tt in range(n):
            for ti in range(1,n+1):
                if (not d[ti] is None) and d[ti] > tt:
                    d[ti] = None
            res = ff(1)
        if res >= inf:
            return 'IMPOSSIBLE'
        return res

    while 1:
        n,m,a,b,c = LI()
        if n == 0:
            break
        rr.append(f(n,m,[a,b,c]))
        break

    return '\n'.join(map(str, rr))

print(main())