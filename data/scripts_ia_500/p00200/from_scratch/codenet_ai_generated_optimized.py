import sys
import heapq

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph_cost = [[] for _ in range(m+1)]
    graph_time = [[] for _ in range(m+1)]
    for _ in range(n):
        a, b, cost, time = map(int, input().split())
        graph_cost[a].append((b, cost))
        graph_cost[b].append((a, cost))
        graph_time[a].append((b, time))
        graph_time[b].append((a, time))

    k = int(input())
    for _ in range(k):
        p, q, r = map(int, input().split())
        if r == 0:
            dist = [float('inf')] * (m+1)
            dist[p] = 0
            heap = [(0, p)]
            while heap:
                cur_cost, u = heapq.heappop(heap)
                if dist[u] < cur_cost:
                    continue
                if u == q:
                    print(cur_cost)
                    break
                for v, c in graph_cost[u]:
                    nc = cur_cost + c
                    if nc < dist[v]:
                        dist[v] = nc
                        heapq.heappush(heap, (nc, v))
        else:
            dist = [float('inf')] * (m+1)
            dist[p] = 0
            heap = [(0, p)]
            while heap:
                cur_time, u = heapq.heappop(heap)
                if dist[u] < cur_time:
                    continue
                if u == q:
                    print(cur_time)
                    break
                for v, t in graph_time[u]:
                    nt = cur_time + t
                    if nt < dist[v]:
                        dist[v] = nt
                        heapq.heappush(heap, (nt, v))