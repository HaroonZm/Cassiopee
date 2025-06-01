import sys
import heapq

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    INF = 10**9
    dist = [[INF, INF] for _ in range(n + 1)]
    dist[1][0] = 0
    heap = [(0, 1, 0)]  # cost, node, used_ticket(0 or 1)

    while heap:
        cost, u, used = heapq.heappop(heap)
        if dist[u][used] < cost:
            continue
        if u == n:
            print(cost)
            break
        if used == 0:
            for v1, c1 in graph[u]:
                # Using ticket starting here if possible (requires two edges)
                for v2, c2 in graph[v1]:
                    if v2 != n:
                        # Take two edges for free
                        if dist[v2][1] > cost:
                            dist[v2][1] = cost
                            heapq.heappush(heap, (cost, v2, 1))
                # Not using ticket, pay edge cost
                if dist[v1][0] > cost + c1:
                    dist[v1][0] = cost + c1
                    heapq.heappush(heap, (cost + c1, v1, 0))
        else:
            # Already used ticket, pay all costs
            for v, c_ in graph[u]:
                if dist[v][1] > cost + c_:
                    dist[v][1] = cost + c_
                    heapq.heappush(heap, (cost + c_, v, 1))