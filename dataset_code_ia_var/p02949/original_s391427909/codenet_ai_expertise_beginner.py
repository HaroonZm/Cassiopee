n, m, p = map(int, input().split())
graph = []
for i in range(n):
    graph.append([])

INF = float("inf")
dist = []
for i in range(n):
    dist.append(INF)
dist[0] = 0

for i in range(m):
    f, t, c = map(int, input().split())
    graph[f - 1].append((t - 1, p - c))

for i in range(n):
    updated = False
    for j in range(n):
        for edge in graph[j]:
            to = edge[0]
            cost = edge[1]
            if dist[j] != INF and dist[to] > dist[j] + cost:
                dist[to] = dist[j] + cost
                updated = True
    if not updated:
        break
else:
    prev_dist = dist[n - 1]
    for k in range(n):
        updated = False
        for j in range(n):
            for edge in graph[j]:
                to = edge[0]
                cost = edge[1]
                if dist[j] != INF and dist[to] > dist[j] + cost:
                    dist[to] = dist[j] + cost
                    updated = True
        if not updated:
            break
    if dist[n - 1] != prev_dist:
        print(-1)
        exit()

answer = dist[n - 1] * (-1)
if answer < 0:
    answer = 0
print(answer)