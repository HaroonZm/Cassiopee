import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

rr = []

while True:
    try:
        n = int(sys.stdin.readline())
    except:
        break
    if n == 0:
        break

    a = []
    for _ in range(n):
        a.append(sys.stdin.readline().split())

    d = collections.defaultdict(int)
    ed = collections.defaultdict(lambda: None)
    for i in range(n):
        x, y, di = a[i]
        x = int(x)
        y = int(y)
        d[(x,y)] = i + 1
        if di == 'x':
            d[(x+1,y)] = i + 1
            ed[(x,y)] = (x+1,y)
            ed[(x+1,y)] = (x,y)
        else:
            d[(x,y+1)] = i + 1
            ed[(x,y)] = (x,y+1)
            ed[(x,y+1)] = (x,y)

    ee = collections.defaultdict(set)
    dka = list(d.keys())
    for x,y in list(d.keys()):
        dt = d[(x,y)]
        for di,dj in dd:
            ni = x + di
            nj = y + dj
            if d[(ni,nj)] > 0 and d[(ni,nj)] != dt:
                ee[(x,y)].add((ni,nj))

    v = collections.defaultdict(bool)
    f = True
    for k in dka:
        if v[k]:
            continue
        s1 = set()
        s2 = set()
        ns1 = set([k])
        ns2 = set()
        while ns1:
            na = list(ns1)
            s1 |= ns1
            ns1 = set()
            for kkk in na:
                ns1 |= ee[kkk]
                ns2.add(ed[kkk])
            ns2 -= s2

            while ns2:
                na2 = list(ns2)
                s2 |= ns2
                ns2 = set()
                for kkk2 in na2:
                    ns2 |= ee[kkk2]
                    ns1.add(ed[kkk2])
                ns2 -= s2

            ns1 -= s1

        if s1 & s2:
            f = False

        if f:
            for kkk in s1:
                v[kkk] = 1
            for kkk in s2:
                v[kkk] = 1
        else:
            break

    if f:
        rr.append('Yes')
    else:
        rr.append('No')

print('\n'.join(map(str,rr)))