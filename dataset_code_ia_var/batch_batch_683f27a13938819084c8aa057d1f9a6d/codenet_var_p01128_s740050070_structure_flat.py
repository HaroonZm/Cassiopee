import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

rr = []

n = int(sys.stdin.readline())
ni = 0

while ni < n:
    ni += 1
    xa,ya,xb,yb = [int(x) for x in sys.stdin.readline().split()]
    a1 = (xa,ya)
    a2 = (xb,yb)
    m = int(sys.stdin.readline())
    a = []
    mi = 0
    while mi < m:
        mi += 1
        a.append([int(x) for x in sys.stdin.readline().split()])
    t = []
    ai = 0
    while ai < len(a):
        xs,ys,xt,yt,o,l = a[ai]
        x1,y1 = a1
        x2,y2 = a2
        x3,y3 = xs,ys
        x4,y4 = xt,yt
        ksi = (y4 - y3) * (x4 - x1) - (x4 - x3) * (y4 - y1)
        eta = (x2 - x1) * (y4 - y1) - (y2 - y1) * (x4 - x1)
        delta = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
        if delta == 0:
            ai += 1
            continue
        ramda = ksi / delta
        mu = eta / delta
        if ramda >= 0 and ramda <= 1 and mu >= 0 and mu <= 1:
            k = (x1 + ramda * (x2 - x1), y1 + ramda * (y2 - y1))
            t.append((k, o ^ l))
        ai += 1
    if len(t) == 0:
        rr.append(0)
        continue
    t.sort()
    c = t[0][1]
    r = 0
    i = 0
    while i < len(t):
        _,tc = t[i]
        if tc != c:
            r += 1
            c = tc
        i += 1
    rr.append(r)

print('\n'.join(map(str,rr)))