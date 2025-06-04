from collections import defaultdict
import heapq
import sys

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7
EPS = 1e-7

def inp():
    return int(input())

def inpl():
    return list(map(int, input().split()))

def inpl_str():
    return input().split()

def dijkstra(graph, n, start):
    dist = [INF] * n
    visited = [False] * n
    hq = [(0, start)]
    dist[start] = 0
    while hq:
        d, u = heapq.heappop(hq)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in graph[u]:
            dv = d + w
            if dv < dist[v]:
                dist[v] = dv
                heapq.heappush(hq, (dv, v))
    return dist

def build_graph(m, reverse=False):
    graph = defaultdict(set)
    for _ in range(m):
        x, y, c = inpl()
        x -= 1
        y -= 1
        if reverse:
            graph[y].add((x, c))
        else:
            graph[x].add((y, c))
    return graph

while True:
    N, M, s, g1, g2 = inpl()
    if N == 0 and M == 0:
        break
    forward_graph = build_graph(M, reverse=False)
    backward_graph = build_graph(M, reverse=True)
    dist_from_s = dijkstra(forward_graph, N, s - 1)
    dist_to_g1 = dijkstra(backward_graph, N, g1 - 1)
    dist_to_g2 = dijkstra(backward_graph, N, g2 - 1)
    print(min((dist_from_s[i] + dist_to_g1[i] + dist_to_g2[i] for i in range(N)), default=INF))