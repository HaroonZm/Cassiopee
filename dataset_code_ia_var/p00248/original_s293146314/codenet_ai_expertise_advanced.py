from sys import stdin
from functools import partial

class UnionFind:
    __slots__ = 'parent', 'size'
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
    def find(self, x: int) -> int:
        p = self.parent
        while x != p[x]:
            p[x] = p[p[x]]
            x = p[x]
        return x
    def unite(self, x: int, y: int) -> bool:
        xroot, yroot = self.find(x), self.find(y)
        if xroot == yroot: return False
        if self.size[xroot] < self.size[yroot]:
            xroot, yroot = yroot, xroot
        self.parent[yroot] = xroot
        self.size[xroot] += self.size[yroot]
        return True
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

input_iter = iter(stdin.readline, '')
nextints = partial(map, int)

while True:
    try:
        n, m = nextints(stdin.readline().split())
        if n == 0: break
        uf = UnionFind(n+1)
        deg = [0] * (n+1)
        valid = True
        for _ in range(m):
            a, b = nextints(stdin.readline().split())
            if not valid:
                continue
            deg[a] += 1
            deg[b] += 1
            if deg[a] > 2 or deg[b] > 2 or not uf.unite(a, b):
                valid = False
        print('yes' if valid else 'no')
    except Exception:
        break