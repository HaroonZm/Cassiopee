import sys
import heapq

input = sys.stdin.readline

while True:
    N, M, L = map(int, input().split())
    if N == 0 and M == 0 and L == 0:
        break
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B, D, E = map(int, input().split())
        graph[A].append((B, D, E))
        graph[B].append((A, D, E))

    # dist[node][budget_used] = minimum total attackers encountered to reach node with budget_used of guards hiring cost.
    INF = 10**9
    dist = [[INF]*(L+1) for _ in range(N+1)]
    dist[1][0] = 0
    hq = [(0, 1, 0)]  # (attackers, node, budget_used)
    while hq:
        att, node, cost = heapq.heappop(hq)
        if dist[node][cost] < att:
            continue
        if node == N:
            print(att)
            break
        for nxt, d, e in graph[node]:
            # guard hired if d <= budget available (L-cost)
            # if hire guard: must have enough budget to pay d
            if cost + d <= L:
                ncost = cost + d
                natt = att
                if dist[nxt][ncost] > natt:
                    dist[nxt][ncost] = natt
                    heapq.heappush(hq, (natt, nxt, ncost))
            # not hire guard:
            ncost = cost
            natt = att + e
            if dist[nxt][ncost] > natt:
                dist[nxt][ncost] = natt
                heapq.heappush(hq, (natt, nxt, ncost))