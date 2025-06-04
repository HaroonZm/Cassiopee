import heapq

# Union find. Not the cleanest...
class UnionFind:
    def __init__(self, n):
        self.size = n
        self.parent = [-1 for _ in range(n)]
    # Who is your root? (Recursion magic here.)
    def find(self, x):
        if self.parent[x] < 0:
            return x
        else:
            # Some kinda path compression
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.parent[a] > self.parent[b]:
            # swap em
            a, b = b, a
        self.parent[a] += self.parent[b]
        self.parent[b] = a

N = int(input())
pts = []
for i in range(N):
    x, y = map(int, input().split())
    pts.append((x, y, i))
# sort by x
pts.sort(key=lambda el: el[0])

edges = []
heapq.heapify(edges)
for idx in range(N-1):
    x1, _, i1 = pts[idx]
    x2, _, i2 = pts[idx+1]
    # shortest x-connection
    heapq.heappush(edges, (x2-x1, i1, i2))
    # print(f"x edge: {i1}-{i2} = {x2-x1}")

# sort by y now
pts.sort(key=lambda el: el[1])
for idx in range(N-1):
    _, y1, i1 = pts[idx]
    _, y2, i2 = pts[idx+1]
    heapq.heappush(edges, (y2-y1, i1, i2))
    # print(f"y edge: {i1}-{i2} = {y2-y1}")

ans = 0
uf = UnionFind(N)

while edges:
    w, a, b = heapq.heappop(edges)
    if uf.find(a) == uf.find(b):
        continue
    uf.union(a, b)
    ans += w
    # print(f'Connect {a} <-> {b}, cost={w}, total={ans}')
# print("done!")
print(ans)
# Hope it works...