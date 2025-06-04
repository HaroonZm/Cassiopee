import heapq
import sys

def dijkstra(n, graph, start, goal):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        cost, u = heapq.heappop(heap)
        if u == goal:
            return cost
        for edge in graph[u]:
            edge_cost, v = edge
            new_cost = cost + edge_cost
            if new_cost < distances[v]:
                distances[v] = new_cost
                heapq.heappush(heap, (new_cost, v))
    return -1

def process_queries(n, k):
    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        line = sys.stdin.readline()
        if line[0] == '0':
            _, s, g = map(int, line.strip().split())
            result = dijkstra(n, graph, s, g)
            print(result)
        else:
            _, a, b, c = map(int, line.strip().split())
            graph[a].append([c, b])
            graph[b].append([c, a])

while True:
    first_line = sys.stdin.readline()
    if first_line == '0 0\n':
        break
    n, k = map(int, first_line.strip().split())
    process_queries(n, k)