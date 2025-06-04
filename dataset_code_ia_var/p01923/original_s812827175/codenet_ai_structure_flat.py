import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

rr = []
while True:
    l = sys.stdin.readline()
    if not l:
        break
    n_m = list(map(int, l.split()))
    if len(n_m) != 2:
        continue
    n, m = n_m
    if n == 0:
        break
    a = []
    for _ in range(n):
        while True:
            x = sys.stdin.readline()
            if x.strip() == "":
                continue
            d_v = list(map(int, x.split()))
            if len(d_v) != 2:
                continue
            a.append(d_v)
            break
    t = collections.defaultdict(int)
    for d, v in a:
        if t[d] < v:
            t[d] = v
    r = 0
    for i in range(1, m+1):
        r += t[i]
    rr.append(r)
print('\n'.join(map(str, rr)))