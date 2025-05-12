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

    def f(n,m,hh,kk):
        e = collections.defaultdict(list)
        for _ in range(m):
            a,b,c,h,r = LI()
            e[a].append((b,c,h,r))
            e[b].append((a,c,h,r))
        ss,tt = LI()
        p = I()
        ps = []
        ii = [2**i for i in range(kk+1)]
        for _ in range(p):
            t = LI()
            d = t[1]
            ks = 0
            for i in t[2:]:
                ks += ii[i]
            ps.append((ks,d))
        pd = collections.defaultdict(lambda: inf)
        pd[0] = 0
        for ks, d in ps:
            for ts, td in list(pd.items()):
                ns = ks | ts
                nd = td + d
                if pd[ns] > nd:
                    pd[ns] = nd
        r = inf
        for ts, td in pd.items():
            ks = set()
            if td >= r:
                continue
            for i in range(kk+1):
                if ts & ii[i]:
                    ks.add(i)

            def search():
                d = collections.defaultdict(lambda: inf)
                d[(ss,0)] = 0
                q = []
                heapq.heappush(q, (0, (ss,0)))
                v = collections.defaultdict(bool)
                while len(q):
                    k, u = heapq.heappop(q)
                    if v[u]:
                        continue
                    v[u] = True
                    if u[0] == tt:
                        return k

                    for uv, ud, uh, ur in e[u[0]]:
                        if u[1] + uh > hh:
                            continue
                        vv = (uv, u[1] + uh)
                        if v[vv]:
                            continue
                        vd = k
                        if ur not in ks:
                            vd += ud
                        if d[vv] > vd:
                            d[vv] = vd
                            heapq.heappush(q, (vd, vv))

                return inf

            tr = search()
            if r > tr + td:
                r = tr + td
            if r == inf:
                break

        if r == inf:
            return -1

        return r

    while 1:
        n,m,h,k = LI()
        if n == 0:
            break
        rr.append(f(n,m,h,k))
        # print('nr',n,rr[-1])

    return '\n'.join(map(str, rr))

print(main())