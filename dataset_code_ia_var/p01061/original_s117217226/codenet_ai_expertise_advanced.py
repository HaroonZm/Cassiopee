from sys import stdin
from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1]*(n+1)
        self.groups = n

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != x:
            x, self.parent[x] = self.parent[x], root
        return root

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.size[xr] < self.size[yr]:
            xr, yr = yr, xr
        self.parent[yr] = xr
        self.size[xr] += self.size[yr]
        self.groups -= 1
        return True

m, n = map(int, stdin.readline().split())
dsu = DSU(m)
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    if not dsu.union(a, b):
        continue
    m -= 1
print(abs(m - dsu.groups))