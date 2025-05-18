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
    rr = []

    def f(n,m,l):
        e = collections.defaultdict(list)
        for _ in range(m):
            a,b,x,y = LI()
            e[a].append((b,x,y))
            e[b].append((a,x,y))

        d = collections.defaultdict(lambda: inf)
        d[(1, 0)] = 0
        q = []
        heapq.heappush(q, (0, 0, 1))
        v = collections.defaultdict(bool)
        mi = inf
        while len(q):
            c, k, u = heapq.heappop(q)
            if v[(u,k)]:
                continue
            v[(u,k)] = True
            if u == n and mi > c:
                mi = c

            for uv, ud, ue in e[u]:
                vk = k + ud
                vv = (uv, vk)
                if not v[vv] and vk <= l:
                    vd = c
                    if d[vv] > vd:
                        d[vv] = vd
                        heapq.heappush(q, (vd, vk, uv))
                vv = (uv, k)
                if not v[vv]:
                    vd = c + ue
                    if d[vv] > vd:
                        d[vv] = vd
                        heapq.heappush(q, (vd, k, uv))

        return mi

    while True:
        n,m,l = LI()
        if n == 0 and m == 0:
            break
        rr.append(f(n,m,l))

    return '\n'.join(map(str, rr))

print(main())