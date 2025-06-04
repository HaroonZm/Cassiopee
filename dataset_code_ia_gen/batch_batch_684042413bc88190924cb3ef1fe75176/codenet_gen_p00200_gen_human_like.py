import sys
import heapq

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    graph_cost = [[] for _ in range(m + 1)]
    graph_time = [[] for _ in range(m + 1)]

    for _ in range(n):
        a, b, cost, time = map(int, input().split())
        graph_cost[a].append((b, cost))
        graph_cost[b].append((a, cost))
        graph_time[a].append((b, time))
        graph_time[b].append((a, time))

    k = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(k)]

    def dijkstra(graph, start, end):
        dist = [float('inf')] * (m + 1)
        dist[start] = 0
        heap = [(0, start)]
        while heap:
            cur_dist, v = heapq.heappop(heap)
            if dist[v] < cur_dist:
                continue
            if v == end:
                return dist[v]
            for nv, cost in graph[v]:
                nd = cur_dist + cost
                if nd < dist[nv]:
                    dist[nv] = nd
                    heapq.heappush(heap, (nd, nv))
        return dist[end]

    for p, q, r in queries:
        if r == 0:
            print(dijkstra(graph_cost, p, q))
        else:
            print(dijkstra(graph_time, p, q))