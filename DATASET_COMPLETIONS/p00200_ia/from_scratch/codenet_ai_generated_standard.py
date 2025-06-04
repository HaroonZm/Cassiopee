import sys
import heapq

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    cost_graph = [[] for _ in range(m + 1)]
    time_graph = [[] for _ in range(m + 1)]
    for _ in range(n):
        a, b, c, t = map(int, input().split())
        cost_graph[a].append((b, c))
        cost_graph[b].append((a, c))
        time_graph[a].append((b, t))
        time_graph[b].append((a, t))
    k = int(input())
    for _ in range(k):
        p, q, r = map(int, input().split())
        dist = [float('inf')] * (m + 1)
        dist[p] = 0
        hq = [(0, p)]
        graph = cost_graph if r == 0 else time_graph
        while hq:
            val, u = heapq.heappop(hq)
            if dist[u] < val:
                continue
            if u == q:
                print(val)
                break
            for v, w in graph[u]:
                nd = val + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(hq, (nd, v))