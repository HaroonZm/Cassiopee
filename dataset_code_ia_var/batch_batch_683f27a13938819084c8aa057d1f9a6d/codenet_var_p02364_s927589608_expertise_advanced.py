from collections import namedtuple

class UnionFind:
    __slots__ = 'par', 'rank', 'siz'
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n
        self.siz = [1] * n

    def find(self, x):
        # Path compression
        px = x
        while self.par[px] != px:
            px = self.par[px]
        while x != px:
            self.par[x], x = px, self.par[x]
        return px

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        # Union by rank
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.par[y] = x
        self.siz[x] += self.siz[y]
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return self.siz[self.find(x)]

def kruskal(n, edges):
    uf = UnionFind(n)
    total = 0
    for w, u, v in edges:
        if uf.unite(u, v):
            total += w
    return total

import sys

Edge = namedtuple('Edge', 'w s t')
V, E = map(int, sys.stdin.readline().split())
es = [tuple(map(int, sys.stdin.readline().split()))[::-1] for _ in range(E)]  # (w, s, t)
es.sort()
print(kruskal(V, es))