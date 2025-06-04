import math

def calc_dist(a, b):
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    dx = x1 - x2
    dy = y1 - y2
    d = math.sqrt(dx * dx + dy * dy)
    return d

class SimpleUnionFind:
    def __init__(self, n):
        self.parent = []
        for i in range(n):
            self.parent.append(i)
        self.rank = []
        for i in range(n):
            self.rank.append(0)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

def kruskal_algo(edge_list, n):
    uf = SimpleUnionFind(n)
    edge_list.sort(key=lambda x: x[2], reverse=True)
    total = 0
    for e in edge_list:
        u = e[0]
        v = e[1]
        w = e[2]
        if not uf.same(u, v):
            uf.unite(u, v)
            total = total + w
    return total

n, m = map(int, input().split())
coords = []
for i in range(n):
    vals = input().split()
    coords.append((int(vals[0]), int(vals[1])))

edges = []
for i in range(m):
    p, q = input().split()
    p = int(p) - 1
    q = int(q) - 1
    d = calc_dist(coords[p], coords[q])
    edges.append((p, q, d))

s = 0
for e in edges:
    s = s + e[2]
ans = s - kruskal_algo(edges, n)
print(ans)