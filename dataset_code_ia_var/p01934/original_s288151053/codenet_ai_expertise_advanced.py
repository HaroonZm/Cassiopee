import sys
import heapq
from itertools import repeat

INF = float('inf')

def dijkstra(V, adj, start, goal, dists):
    dist = [INF] * V
    dist[start] = 0
    heap = [(0, start)]
    visited = [False] * V

    while heap:
        cost, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        if u == goal:
            return cost
        for v in adj[u]:
            new_cost = cost + (dists[v] if v > u else 0)
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(heap, (new_cost, v))
    return -1

def main():
    N, M, s, t, *rest = map(int, sys.stdin.read().split())
    s -= 1
    t -= 1
    d = rest[:N]
    edges = rest[N:]
    if s >= t:
        print(0)
        return
    adj = [[i-1] if i else [] for i in range(N)]
    for a, b in zip(edges[::2], edges[1::2]):
        adj[a-1].append(b-1)
    print(dijkstra(N, adj, s, t, d))

if __name__ == '__main__':
    main()