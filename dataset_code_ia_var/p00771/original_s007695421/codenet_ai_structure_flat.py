import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

eps = 1e-7
rr = []

while True:
    line = sys.stdin.readline()
    if not line:
        break
    n = int(line)
    if n == 0:
        break
    a = []
    for _ in range(n):
        a.append([int(x) for x in sys.stdin.readline().split()])
    # Plateau bissection excessively flat
    mi_y = -100
    ma_y = 100
    while ma_y > mi_y + eps:
        m1y = (mi_y*2+ma_y)/3.0
        m2y = (mi_y+ma_y*2)/3.0
        # For m1y
        mi_x = -100
        ma_x = 100
        while ma_x > mi_x + eps:
            m1x = (mi_x*2+ma_x)/3.0
            m2x = (mi_x+ma_x*2)/3.0
            r1 = inf
            for px,py,l in a:
                v1 = l**2 - (m1x-px)**2 - (m1y-py)**2
                r1 = min(r1, v1)
            r2 = inf
            for px,py,l in a:
                v2 = l**2 - (m2x-px)**2 - (m1y-py)**2
                r2 = min(r2, v2)
            if r1 < r2:
                mi_x = m1x
            else:
                ma_x = m2x
        res1 = inf
        x0 = (ma_x+mi_x)/2.0
        for px,py,l in a:
            v0 = l**2 - (x0-px)**2 - (m1y-py)**2
            res1 = min(res1, v0)
        # For m2y
        mi_x = -100
        ma_x = 100
        while ma_x > mi_x + eps:
            m1x = (mi_x*2+ma_x)/3.0
            m2x = (mi_x+ma_x*2)/3.0
            r1 = inf
            for px,py,l in a:
                v1 = l**2 - (m1x-px)**2 - (m2y-py)**2
                r1 = min(r1, v1)
            r2 = inf
            for px,py,l in a:
                v2 = l**2 - (m2x-px)**2 - (m2y-py)**2
                r2 = min(r2, v2)
            if r1 < r2:
                mi_x = m1x
            else:
                ma_x = m2x
        res2 = inf
        x0 = (ma_x+mi_x)/2.0
        for px,py,l in a:
            v0 = l**2 - (x0-px)**2 - (m2y-py)**2
            res2 = min(res2, v0)
        if res1 < res2:
            mi_y = m1y
        else:
            ma_y = m2y
    y0 = (ma_y+mi_y)/2.0
    mi_x = -100
    ma_x = 100
    while ma_x > mi_x + eps:
        m1x = (mi_x*2+ma_x)/3.0
        m2x = (mi_x+ma_x*2)/3.0
        r1 = inf
        for px,py,l in a:
            v1 = l**2 - (m1x-px)**2 - (y0-py)**2
            r1 = min(r1, v1)
        r2 = inf
        for px,py,l in a:
            v2 = l**2 - (m2x-px)**2 - (y0-py)**2
            r2 = min(r2, v2)
        if r1 < r2:
            mi_x = m1x
        else:
            ma_x = m2x
    x0 = (ma_x+mi_x)/2.0
    rfin = inf
    for px,py,l in a:
        v0 = l**2 - (x0-px)**2 - (y0-py)**2
        rfin = min(rfin, v0)
    rr.append("{:0.7f}".format(rfin**0.5))
print('\n'.join(map(str,rr)))