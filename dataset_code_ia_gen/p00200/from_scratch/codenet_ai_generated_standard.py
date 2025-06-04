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
        a, b, c, t = map(int, input().split())
        graph_cost[a].append((b, c))
        graph_cost[b].append((a, c))
        graph_time[a].append((b, t))
        graph_time[b].append((a, t))

    k = int(input())
    for _ in range(k):
        p, q, r = map(int, input().split())
        if r == 0:
            dist = [float('inf')] * (m+1)
            dist[p] = 0
            heap = [(0, p)]
            while heap:
                cost, node = heapq.heappop(heap)
                if dist[node] < cost:
                    continue
                if node == q:
                    print(cost)
                    break
                for nxt, c in graph_cost[node]:
                    new_cost = cost + c
                    if dist[nxt] > new_cost:
                        dist[nxt] = new_cost
                        heapq.heappush(heap, (new_cost, nxt))
        else:
            dist = [float('inf')] * (m+1)
            dist[p] = 0
            heap = [(0, p)]
            while heap:
                time_, node = heapq.heappop(heap)
                if dist[node] < time_:
                    continue
                if node == q:
                    print(time_)
                    break
                for nxt, t_ in graph_time[node]:
                    new_time = time_ + t_
                    if dist[nxt] > new_time:
                        dist[nxt] = new_time
                        heapq.heappush(heap, (new_time, nxt))