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

def intersection(a1, a2, b1, b2):
    x1,y1 = a1
    x2,y2 = a2
    x3,y3 = b1
    x4,y4 = b2

    ksi = (y4 - y3) * (x4 - x1) - (x4 - x3) * (y4 - y1)
    eta = (x2 - x1) * (y4 - y1) - (y2 - y1) * (x4 - x1)
    delta = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
    if delta == 0:
        return None
    ramda = ksi / delta;
    mu = eta / delta;
    if ramda >= 0 and ramda <= 1 and mu >= 0 and mu <= 1:
        return (x1 + ramda * (x2 - x1), y1 + ramda * (y2 - y1))

    return None

def main():
    rr = []

    n = I()
    ni = 0

    while ni < n:
        ni += 1
        xa,ya,xb,yb = LI()
        a1 = (xa,ya)
        a2 = (xb,yb)
        m = I()
        a = [LI() for _ in range(m)]
        t = []
        for xs,ys,xt,yt,o,l in a:
            k = intersection(a1,a2,(xs,ys),(xt,yt))
            if k is None:
                continue
            t.append((k,o^l))
        if len(t) == 0:
            rr.append(0)
            continue

        t.sort()
        c = t[0][1]
        r = 0
        for _,tc in t:
            if tc != c:
                r += 1
                c = tc

        rr.append(r)

    return '\n'.join(map(str, rr))

print(main())