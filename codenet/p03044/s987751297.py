from collections import deque

n = int(input())
neighbor = {}
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    if u not in neighbor:
        neighbor[u] = deque()
    if v not in neighbor:
        neighbor[v] = deque()
    neighbor[u].append((v, w))
    neighbor[v].append((u, w))

color = {1: 0}
visited = set([1])
queue = deque([(1, 0)])

while len(queue) > 0:
    v, wsum = queue.pop()
    for u, w in neighbor[v]:
        if u in visited:
            continue
        visited.add(u)
        color[u] = (wsum + w) % 2
        queue.append((u, wsum + w))

for i in range(n):
    print(color[i + 1])