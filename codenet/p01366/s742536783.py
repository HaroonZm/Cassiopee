from heapq import heappush, heappop

def dijkstra(edges, size, source):
    distance = [float('inf')] * size
    distance[source] = 0
    visited = [False] * size
    pq = []
    heappush(pq, (0, source))
    while pq:
        dist_u, u = heappop(pq)
        visited[u] = True
        for v, weight, _ in edges[u]:
            if not visited[v]:
                new_dist = dist_u + weight
                if distance[v] > new_dist:
                    distance[v] = new_dist
                    heappush(pq, (new_dist, v))
    return distance

while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    edges = [[] for i in range(N)]

    for i in range(M):
        u, v, d, c = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append((v, d, c))
        edges[v].append((u, d, c))

    dist = dijkstra(edges, N, 0)
    ans = 0
    for u in range(1, N):
        cost = 1000
        for v, d, c in edges[u]:
            if dist[u] == dist[v] + d:
                cost = min(cost, c)
        ans += cost
    print(ans)