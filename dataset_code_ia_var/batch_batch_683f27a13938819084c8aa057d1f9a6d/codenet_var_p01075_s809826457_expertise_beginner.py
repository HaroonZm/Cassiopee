import heapq

def dijkstra(n, graph, start):
    INF = 2147483647
    dist = [INF] * n
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        cur_cost, u = heapq.heappop(pq)
        if cur_cost > dist[u]:
            continue
        for (v, cost) in graph[u]:
            if cur_cost <= cost and cost < dist[v]:
                dist[v] = cost
                heapq.heappush(pq, (cost, v))
    return dist

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
edges_to_last = []

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c))
    if b == n - 1:
        edges_to_last.append((a, c))

distances = dijkstra(n, graph, 0)
if distances[n-1] == 2147483647:
    print(-1)
else:
    edges_to_last.sort(key=lambda x: -x[1])
    for a, c in edges_to_last:
        if distances[a] <= c:
            print(c)
            break