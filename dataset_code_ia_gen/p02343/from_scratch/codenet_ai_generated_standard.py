class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def unite(self, x, y):
        xroot, yroot = self.find(x), self.find(y)
        if xroot == yroot:
            return
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

n, q = map(int, input().split())
ds = DisjointSet(n)
for _ in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        ds.unite(x, y)
    else:
        print(1 if ds.same(x, y) else 0)