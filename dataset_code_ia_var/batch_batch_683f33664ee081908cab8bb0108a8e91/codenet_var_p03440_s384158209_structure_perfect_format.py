N, M = map(int, input().split())
A = list(map(int, input().split()))
XY = [tuple(map(int, input().split())) for _ in range(M)]

class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [0] * N
        self.count = 0
    def root(self, a):
        if self.parent[a] == a:
            return a
        else:
            self.parent[a] = self.root(self.parent[a])
            return self.parent[a]
    def is_same(self, a, b):
        return self.root(a) == self.root(b)
    def unite(self, a, b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        else:
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]:
                self.rank[ra] += 1
        self.count += 1

uf = UnionFind(N)
for x, y in XY:
    if uf.is_same(x, y):
        continue
    uf.unite(x, y)
for i in range(N):
    uf.root(i)

c = N - uf.count
if c == 1:
    print(0)
    exit()
ex = c - 2
if c + ex > N:
    print('Impossible')
    exit()

from collections import defaultdict
d = defaultdict(lambda: [])
for i, a in enumerate(A):
    r = uf.root(i)
    d[r].append(a)

ans = 0
hq = []
for k in d.keys():
    s = sorted(d[k])
    ans += s[0]
    for v in s[1:]:
        hq.append(v)

import heapq
heapq.heapify(hq)
for _ in range(ex):
    v = heapq.heappop(hq)
    ans += v
print(ans)