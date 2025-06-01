class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, x, y):
        xroot, yroot = self.find(x), self.find(y)
        if xroot == yroot:
            return False
        if self.size[xroot] < self.size[yroot]:
            xroot, yroot = yroot, xroot
        self.parent[yroot] = xroot
        self.size[xroot] += self.size[yroot]
        return True
    def connected(self, x, y):
        return self.find(x) == self.find(y)

import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    uf = UnionFind(n+1)
    degree = [0]*(n+1)
    ans = True
    for _ in range(m):
        a, b = map(int, input().split())
        if ans:
            degree[a] += 1
            degree[b] += 1
            if degree[a] > 2 or degree[b] > 2 or uf.connected(a, b):
                ans = False
            else:
                uf.union(a, b)
    print("yes" if ans else "no")