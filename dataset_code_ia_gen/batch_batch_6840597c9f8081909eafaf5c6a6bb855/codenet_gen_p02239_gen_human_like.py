n = int(input())
graph = {}
for _ in range(n):
    data = list(map(int, input().split()))
    u = data[0]
    k = data[1]
    graph[u] = data[2:] if k > 0 else []

dist = [-1] * (n + 1)
dist[1] = 0

from collections import deque
queue = deque([1])

while queue:
    u = queue.popleft()
    for v in graph[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            queue.append(v)

for i in range(1, n + 1):
    print(i, dist[i])