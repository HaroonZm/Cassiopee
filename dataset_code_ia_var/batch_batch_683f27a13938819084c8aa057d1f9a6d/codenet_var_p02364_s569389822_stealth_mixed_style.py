import heapq

class DisjointSet:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0]*n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.find(self.p[x])
            x = self.p[x]
        return x
    def unite(self, x, y):
        a = self.find(x)
        b = self.find(y)
        if self.rank[a] > self.rank[b]: self.p[b]=a
        elif self.rank[a] < self.rank[b]: self.p[a]=b
        else:
            self.p[a]=b
            self.rank[b]+=1

v,e = [int(i) for i in input().split()]
ds = DisjointSet(v)
class Edge: pass
edges = []
for _ in range(e):
    x = Edge(); x.u,x.v,x.w = map(int, input().split())
    heapq.heappush(edges, (x.w, x.u, x.v))

total = 0
get = lambda: heapq.heappop(edges) if edges else None
def process():
    while edges:
        w, a, b = get()
        if ds.find(a) != ds.find(b):
            ds.unite(a, b)
            globals()['total'] += w
process()
print(total)