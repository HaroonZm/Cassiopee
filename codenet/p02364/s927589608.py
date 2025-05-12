class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.siz = [1 for i in range(n)]
    
    def find(self, x):
        if self.par[x] == x:
            return x
        return self.find(self.par[x])
    
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] > self.rank[y]:
            self.par[y] = x
            self.siz[x] += self.siz[y]
        else:
            self.par[x] = y
            self.siz[y] += self.siz[x]
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def size(self, x):
        return self.siz[self.find(x)]
    
def kruskal(n, m):
    res = 0
    uf = UnionFind(n)
    for i in range(m):
        w, s, t = es[i]
        if uf.same(s, t):
            continue
        uf.unite(s, t)
        res += w
    return res

V, E = map(int, input().split())
es = []
for i in range(E):
    s, t, w = map(int, input().split())
    es.append([w, s, t])

es.sort(key=lambda x: x[0])
res = kruskal(V, E)
print(res)