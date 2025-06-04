class SimpleUnionFind:
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.parent[y_root] < self.parent[x_root]:
            x_root, y_root = y_root, x_root
        self.parent[x_root] += self.parent[y_root]
        self.parent[y_root] = x_root

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def group_size(self, x):
        return -self.parent[self.find(x)]

n, m = map(int, input().split())
uf = SimpleUnionFind(n)
coordinates = []
graph = []
for i in range(n):
    coordinates.append(tuple(map(int, input().split())))
for i in range(n):
    graph.append([])

total_length = 0.0

for j in range(m):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    uf.union(p, q)
    x1, y1 = coordinates[p]
    x2, y2 = coordinates[q]
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    graph[p].append((-dist, q))
    graph[q].append((-dist, p))
    total_length += dist

from heapq import heappush, heappop, heapify

visited = [False] * n
answer = 0.0

for i in range(n):
    if uf.parent[i] >= 0:
        continue
    queue = []
    for cost, neighbor in graph[i]:
        queue.append((cost, neighbor))
    visited[i] = True
    heapify(queue)
    while queue:
        cost, v = heappop(queue)
        if visited[v]:
            continue
        visited[v] = True
        answer -= cost
        for next_cost, next_v in graph[v]:
            if not visited[next_v]:
                heappush(queue, (next_cost, next_v))

print(total_length - answer)