import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

class UnionFind:
    def __init__(self, size):
        self.rank = [0] * size
        self.par = range(size)
        self.g_num = size

    def find(self, x):
        if x == self.par[x]: return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return

        self.g_num -= 1
        if (self.rank[x] > self.rank[y]):
            self.par[y] = x
        else:
            self.par[x] = y
            if (self.rank[x] == self.rank[y]): self.rank[y] += 1

    def group_num(self):
        return self.g_num

N, M = map(int, raw_input().split())
L = [map(int, raw_input().split()) for i in xrange(N)]

sp = [-1]*M
uf = UnionFind(N)
for i in xrange(N):
    k = L[i][0]
    for j in xrange(1, k + 1):
        if sp[L[i][j] - 1] == -1:
            sp[L[i][j] - 1] = i
        else:
            uf.unite(sp[L[i][j] - 1], i)

print "YES" if uf.group_num() == 1 else "NO"