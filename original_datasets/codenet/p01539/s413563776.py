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
    dd0 = [(0,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(0,0)]
    dd1 = [(0,1),(1,1),(1,0),(0,-1),(-1,0),(-1,1),(0,0)]
    dd = [dd0, dd1]

    def f(n):
        sx,sy,gx,gy = LI()
        n = I()
        fs = set([tuple(LI()) for _ in range(n)])
        lx,ly = LI()

        def search(s, g):
            d = collections.defaultdict(lambda: inf)
            s = tuple(list(s) + [0])
            d[s] = 0
            q = []
            heapq.heappush(q, (0, s))
            v = collections.defaultdict(bool)
            while len(q):
                k, u = heapq.heappop(q)
                if v[u]:
                    continue
                if (u[0],u[1]) == g:
                    return k
                v[u] = True
                ddi = 0 if u[0] % 2 == 0 else 1
                di,dj = dd[ddi][abs(u[0]*u[1]*u[2])%6]
                nu = (u[2] + 1) % 6
                uv = (u[0]+di, u[1]+dj, nu)
                if d[uv] > k and abs(uv[0]) <= lx and abs(uv[1]) <= ly and not ((uv[0],uv[1]) in fs):
                    d[uv] = k
                    heapq.heappush(q, (k, uv))

                vd = k + 1
                for di,dj in dd[ddi]:
                    uv = (u[0]+di, u[1]+dj, nu)
                    if v[uv] or abs(uv[0]) > lx or abs(uv[1]) > ly or (uv[0],uv[1]) in fs:
                        continue
                    if d[uv] > vd:
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))

            return None
        r = search((sx,sy),(gx,gy))
        if r is None:
            return -1
        return r

    while 1:
        n = 1
        if n == 0:
            break
        rr.append(f(n))
        break
        # print('rr', rr[-1])

    return '\n'.join(map(str,rr))

print(main())