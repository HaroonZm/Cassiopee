from heapq import heappush, heappop

def dijkstra(s, t, graph):
    heap = [(cost, neighbor) for cost, neighbor in graph[s]]
    heapify(heap := heap or [(0, s)])
    visited = set()
    while heap:
        cost, node = heappop(heap)
        if node == t:
            return cost
        if node in visited:
            continue
        visited.add(node)
        for c, nxt in graph[node]:
            if nxt not in visited:
                heappush(heap, (cost + c, nxt))
    return -1

import sys
input = sys.stdin.readline

while True:
    n, k = map(int, input().split())
    if n == 0:
        break
    graph = [set() for _ in range(n)]
    for _ in range(k):
        *data, = map(int, input().split())
        if data[0]:
            c, d, e = data
            c -= 1; d -= 1
            graph[c].add((e, d))
            graph[d].add((e, c))
        else:
            a, b = data[1], data[2]
            print(dijkstra(a - 1, b - 1, graph))