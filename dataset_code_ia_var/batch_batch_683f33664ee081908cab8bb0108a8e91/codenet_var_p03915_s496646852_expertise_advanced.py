import sys
from operator import itemgetter
from functools import partial

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

N, Q = map(int, readline().split())
data = list(map(int, read().split()))
ABC = list(zip(*[iter(data)]*3))

INF = 10**18
cyclic_cost = [INF] * N

for a, b, c in ABC:
    cyclic_cost[a] = min(cyclic_cost[a], c + 1)
    cyclic_cost[b] = min(cyclic_cost[b], c + 2)

# Extend to 2N for cyclic process
cyclic_cost = cyclic_cost * 2

x = INF
for i, cost in enumerate(cyclic_cost):
    x += 2
    if x < cost:
        cyclic_cost[i] = x
    x = cyclic_cost[i]

min_cyc = list(map(min, zip(cyclic_cost[:N], cyclic_cost[N:])))
edges = [*ABC, *( (i, (i+1)%N, c) for i, c in enumerate(min_cyc) )]
edges[-1] = (N-1, 0, min_cyc[-1])

class UnionFind:
    __slots__ = ('root', 'size')
    def __init__(self, n):
        self.root = list(range(n))
        self.size = [1]*n
    def find(self, x):
        r = self.root
        while r[x] != x:
            r[x] = r[r[x]]
            x = r[x]
        return x
    def merge(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return False
        sizex, sizey = self.size[xr], self.size[yr]
        if sizex < sizey:
            self.root[xr] = yr
            self.size[yr] += sizex
        else:
            self.root[yr] = xr
            self.size[xr] += sizey
        return True

edges.sort(key=itemgetter(2))

uf = UnionFind(N)
total = 0
for a, b, c in edges:
    if uf.merge(a, b):
        total += c
print(total)