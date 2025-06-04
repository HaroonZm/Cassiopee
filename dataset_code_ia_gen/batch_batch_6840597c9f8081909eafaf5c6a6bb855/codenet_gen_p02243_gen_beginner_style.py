n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n):
    data = list(map(int, input().split()))
    u = data[0]
    k = data[1]
    for i in range(k):
        v = data[2 + 2*i]
        c = data[3 + 2*i]
        graph[u].append((v, c))

dist = [float('inf')] * n
dist[0] = 0

# Simple approach similar to Bellman-Ford but repeated n times (inefficient)
for _ in range(n):
    updated = False
    for u in range(n):
        for (v, c) in graph[u]:
            if dist[u] + c < dist[v]:
                dist[v] = dist[u] + c
                updated = True
    if not updated:
        break

for u in range(n):
    print(u, dist[u])