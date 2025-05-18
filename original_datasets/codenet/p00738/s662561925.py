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

def ky(p1, p2):
    return pow(pow(p1[0]-p2[0], 2) + pow(p1[1]-p2[1], 2), 0.5)

def distance3(p1, p2, p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3

    ax = x2 - x1
    ay = y2 - y1
    bx = x3 - x1
    by = y3 - y1

    r = (ax*bx + ay*by) / (ax*ax + ay*ay)
    if r <= 0:
        return ky(p1, p3)
    if r >= 1:
        return ky(p2, p3)
    pt = (x1 + r*ax, y1 + r*ay, 0)
    return ky(pt, p3)

def main():
    rr = []

    def f(n):
        sx,sy,ex,ey = LI()
        sp = (sx,sy)
        ep = (ex,ey)
        a = [LI() for _ in range(n)]
        td = collections.defaultdict(lambda: inf)
        for x1,y1,x2,y2,h in a:
            ps = [(x1,y1), (x1,y2), (x2,y1), (x2,y2)]
            for p1,p2 in itertools.combinations(ps, 2):
                if kosa(sp,ep,p1,p2):
                    return 0
                for p in [sp,ep]:
                    dc = distance3(p1,p2,p)
                    if td[h] > dc:
                        td[h] = dc

            for p in ps:
                dc = distance3(sp,ep,p)
                if td[h] > dc:
                    td[h] = dc

        r = 1000
        for h,k in td.items():
            if k < h:
                if r > k:
                    r = k
                continue
            tr = 1.0 * (h**2 + k**2) / h / 2
            if r > tr:
                r = tr

        return '{:0.4f}'.format(r)

    while 1:
        n = I()
        if n == 0:
            break
        rr.append(f(n))
        # print('rr', rr[-1])

    return '\n'.join(map(str,rr))

print(main())