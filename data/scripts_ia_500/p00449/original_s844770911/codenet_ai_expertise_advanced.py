from heapq import heappush, heappop
import sys

input = sys.stdin.readline

def dijkstra(n, graph, start, goal):
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cost, node = heappop(heap)
        if node == goal:
            return cost
        if cost > dist[node]:
            continue
        for weight, neighbor in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heappush(heap, (new_cost, neighbor))
    return -1

def process(n, q):
    graph = [[] for _ in range(n)]
    for _ in range(q):
        line = input()
        op, *args = line.split()
        if op == '0':
            s, g = map(int, args)
            print(dijkstra(n, graph, s, g))
        else:
            c, d, e = map(int, args)
            graph[c].append((e, d))
            graph[d].append((e, c))

for line in iter(input, '0 0\n'):
    n, k = map(int, line.split())
    process(n, k)