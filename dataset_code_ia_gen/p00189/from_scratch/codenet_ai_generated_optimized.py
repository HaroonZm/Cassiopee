import sys
import heapq

input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    edges = [tuple(map(int, input().split())) for _ in range(n)]
    towns = set()
    for a, b, c in edges:
        towns.add(a)
        towns.add(b)
    N = max(towns)+1
    graph = [[] for _ in range(N)]
    for a, b, c in edges:
        graph[a].append((b, c))
        graph[b].append((a, c))
    def dijkstra(s):
        dist = [float('inf')] * N
        dist[s] = 0
        hq = [(0, s)]
        while hq:
            cd, u = heapq.heappop(hq)
            if dist[u] < cd:
                continue
            for v, cost in graph[u]:
                nd = cd + cost
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(hq, (nd, v))
        return dist
    min_sum = float('inf')
    ans = 0
    for i in range(N):
        dist = dijkstra(i)
        s = sum(dist)
        if s < min_sum:
            min_sum = s
            ans = i
    print(ans, min_sum)