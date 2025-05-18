def dist(c1, c2):
    return ((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)**.5

def kruskal(edges, size):
    uf = UnionFind(size)
    edges = sorted(edges, key=lambda e: e[2])[::-1]
    ret = 0
    for u, v, weight in edges:
        if not uf.same(u, v):
            uf.unite(u, v)
            ret += weight
    return ret

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

N, M = map(int, input().split())
coords = [tuple(map(int, input().split())) for i in range(N)]
edges = []
for i in range(M):
    p, q = map(lambda x: int(x) - 1, input().split())
    edges.append((p, q, dist(coords[p], coords[q])))
print(sum(e[2] for e in edges) - kruskal(edges, N))