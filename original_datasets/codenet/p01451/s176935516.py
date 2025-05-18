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

def _kosa(a1, a2, b1, b2):
    x1,y1 = a1
    x2,y2 = a2
    x3,y3 = b1
    x4,y4 = b2

    tc = (x1-x2)*(y3-y1)+(y1-y2)*(x1-x3)
    td = (x1-x2)*(y4-y1)+(y1-y2)*(x1-x4)
    return tc*td < 0

def kosa(a1, a2, b1, b2):
    return _kosa(a1,a2,b1,b2) and _kosa(b1,b2,a1,a2)

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def distance_p(a, b):
    return distance(a[0], a[1], b[0], b[1])

def main():
    rr = []

    def f(n,m):
        a = [LI() for _ in range(n)]
        b = [LI() for _ in range(m)]

        def search(a,b1,b2,rg):
            d = collections.defaultdict(lambda: inf)
            s = 0
            t = 1
            d[s] = 0
            q = []
            heapq.heappush(q, (0, s))
            v = collections.defaultdict(bool)
            while len(q):
                k, u = heapq.heappop(q)
                if v[u]:
                    continue
                v[u] = True
                if u == t:
                    return d[u]

                for uv in rg:
                    if v[uv]:
                        continue
                    if kosa(a[u],a[uv], b1,b2):
                        continue
                    ud = distance_p(a[u],a[uv])
                    vd = k + ud
                    if d[uv] > vd:
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))

            return -1

        ad = distance_p(a[0], a[1])
        bd = distance_p(b[0], b[1])
        ar = search(a,b[0],b[1],list(range(1,n)))
        br = search(b,a[0],a[1],list(range(1,m)))
        r = -1
        if ar < 0:
            if br < 0:
                return r
            return '{:0.9f}'.format(br + ad)
        if br < 0:
            return '{:0.9f}'.format(ar + bd)

        return '{:0.9f}'.format(min(ar + bd, br + ad))

    while 1:
        n,m = LI()
        if n == 0:
            break
        rr.append(f(n,m))
        # print(n, rr[-1])
        break

    return '\n'.join(map(str, rr))

print(main())