class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.r = [0]*n
        self.size_dict = dict((i, 1) for i in range(n))
        self.count = n

    def root(self, v):
        while self.parent[v] != v:
            v = self.parent[v]
        return v

    def link(self, a, b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb:
            return
        if self.r[ra] < self.r[rb]:
            self.parent[ra] = rb
            self.size_dict[rb] += self.size_dict[ra]
        else:
            self.parent[rb] = ra
            self.size_dict[ra] += self.size_dict[rb]
            if self.r[ra] == self.r[rb]: self.r[ra] += 1
        self.count -= 1

    def connected(self, a, b):
        return self.root(a) == self.root(b)

    def component_size(self, a):
        return self.size_dict[self.root(a)]

def k(N, M):
    total = 0
    ufset = UF(N)
    idx = 0
    while idx < M:
        edge = es[idx]
        weight, u, v = edge
        if not ufset.connected(u, v):
            ufset.link(u, v)
            total += weight
        idx += 1
    return total

[V, E] = list(map(int, input().split()))
es = []
for _ in range(E):
    a, b, c = [int(s) for s in input().split()]
    tup = [c, a, b]
    es.append(tup)
es = sorted(es)
result = k(V, E)
print(result)