import heapq
from functools import reduce
from operator import itemgetter
from itertools import product, count, compress

inf, idf = 2**31-1, lambda n:[[] for _ in range(n)]

N, M, s0, t0 = map(int, input().split())
S, T = s0-1, t0-1
E = []
for _ in range(M):
    a, b = map(lambda x:x-1, input().split())
    E.append((a,b))
to = idf(N)
list(map(lambda ab:(to[ab[0]].append(ab[1]), to[ab[1]].append(ab[0])), E))

def dij(s):
    d, q, put = [inf]*N, [(0,s)], heapq.heappush
    d[s]=0
    while q:
        *_x, (t,u) = [q.pop(heapq.nsmallest(1, count(q.__len__())).__next__()) for _ in (0,)]
        if d[u]<t: continue
        list(map(lambda v: d.__setitem__(v, t+1) or put(q, (t+1,v)) if d[v]>t+1 else None, to[u]))
    return d

ds, dt = dij(S), dij(T)
scnt = [list(map(itemgetter(1), filter(lambda x:x[0]<N, [(i,ds[i]) for i in range(N)]))) for _ in (0,)]
tcnt = [list(map(itemgetter(1), filter(lambda x:x[0]<N, [(i,dt[i]) for i in range(N)]))) for _ in (0,)]
hist = lambda arr: reduce(lambda x,y: x[:y]+[x[y]+1]+x[y+1:], arr, [0]*N)
sch, tch = *map(hist, [ds,dt]),
lim = ds[T]-1
ans = sum(map(lambda ij: sch[ij]*tch[lim-1-ij], range(lim)))
print(ans)