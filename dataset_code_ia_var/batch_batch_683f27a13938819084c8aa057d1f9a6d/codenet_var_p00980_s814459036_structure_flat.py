import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

w,h,n = list(map(int, sys.stdin.readline().split()))
aa = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = []
r = [[None]*w for _ in range(h)]
for x,y,z in aa:
    r[y-1][x-1] = z
    heapq.heappush(q, (-z, (y-1,x-1)))

v = collections.defaultdict(bool)
_ret = None
while len(q):
    k, u = heapq.heappop(q)
    if v[u]:
        continue
    v[u] = True
    y = u[0]
    x = u[1]
    for dy,dx in dd:
        uy = y + dy
        ux = x + dx
        if uy < 0 or uy >= h or ux < 0 or ux >= w:
            continue
        uv = (uy,ux)
        if v[uv]:
            continue
        vd = -k - 1
        if r[uy][ux] is None:
            r[uy][ux] = vd
            heapq.heappush(q, (-vd, uv))
        else:
            if abs(r[uy][ux] + k) > 1:
                print('No')
                sys.exit(0)
print(sum(sum(_) for _ in r))