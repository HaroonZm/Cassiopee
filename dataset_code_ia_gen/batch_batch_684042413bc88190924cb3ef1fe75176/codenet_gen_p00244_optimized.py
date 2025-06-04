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

    # dist[node][state]: minimal cost to reach node with state (0:not used free ticket, 1:used free ticket)
    dist = [[float('inf')] * 2 for _ in range(n + 1)]
    dist[1][0] = 0
    hq = [(0, 1, 0)]  # cost, node, state

    while hq:
        cost, u, used = heapq.heappop(hq)
        if dist[u][used] < cost:
            continue
        if u == n:
            print(cost)
            break
        if used == 0:
            # Try to use the free ticket on two consecutive edges
            for v1, c1 in graph[u]:
                if v1 == n:
                    continue  # Cannot use free ticket if destination on intermediate step
                for v2, c2 in graph[v1]:
                    if v2 == n:
                        continue
                    new_cost = cost
                    if dist[v2][1] > new_cost:
                        dist[v2][1] = new_cost
                        heapq.heappush(hq, (new_cost, v2, 1))
        # Normal movement without free ticket or after using it
        for v, c in graph[u]:
            new_cost = cost + c
            if dist[v][used] > new_cost:
                dist[v][used] = new_cost
                heapq.heappush(hq, (new_cost, v, used))