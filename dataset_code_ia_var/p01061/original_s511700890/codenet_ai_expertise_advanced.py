from sys import stdin
from collections import Counter

class UnionFind:
    __slots__ = ('parent', 'size')

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        root = x
        path = []
        while root != self.parent[root]:
            path.append(root)
            root = self.parent[root]
        for v in path:
            self.parent[v] = root
        return root

    def unite(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return
        if self.size[x_root] < self.size[y_root]:
            x_root, y_root = y_root, x_root
        self.parent[y_root] = x_root
        self.size[x_root] += self.size[y_root]

N, M = map(int, stdin.readline().split())
uf = UnionFind(N + 1)

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    uf.unite(a, b)

roots = (uf.find(i) for i in range(1, N + 1))
component_sizes = Counter(roots)

singletons = sum(1 for c in component_sizes.values() if c == 1)
clusters = sum(1 for c in component_sizes.values() if c > 1)

print(abs(singletons - clusters))