import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

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
    s = sys.stdin.readline().strip()
    k = sys.stdin.readline().strip()
    l = len(k)
    if s == k:
        rr.append(0)
        continue
    u = set([s])
    c = set([s])
    t = 0
    r = -1
    while c:
        t += 1
        ns = set()
        for cs in c:
            for d, e in a:
                nt = cs.replace(d, e)
                if len(nt) > l:
                    continue
                ns.add(nt)
        if k in ns:
            r = t
            break
        c = ns - u
        u |= ns
    rr.append(r)
print('\n'.join(map(str, rr)))