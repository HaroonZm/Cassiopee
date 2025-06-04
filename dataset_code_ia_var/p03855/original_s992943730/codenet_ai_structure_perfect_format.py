import sys
from collections import defaultdict

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

N, K, L = map(int, input().split())

ufl = UnionFind(N)
uft = UnionFind(N)

for _ in range(K):
    p, q = map(int, readline().split())
    ufl.union(p - 1, q - 1)

for _ in range(L):
    r, s = map(int, readline().split())
    uft.union(r - 1, s - 1)

grp = [(ufl.find(i), uft.find(i)) for i in range(N)]

dd = defaultdict(int)
for g in grp:
    dd[g] += 1

ans = []
for i in range(N):
    ans.append(dd[grp[i]])

print(' '.join(map(str, ans)))