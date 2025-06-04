import sys
import heapq

while True:
    N, M, L, K, A, H = map(int, raw_input().split())
    if N == 0:
        break
    Ls = map(int, raw_input().split())
    edge = {}
    for l in Ls:
        for i in xrange(M):
            edge[l * (M + 1) + i] = [(l * (M + 1) + i + 1, 1)]
    for _ in xrange(K):
        s, g, c = map(int, raw_input().split())
        for i in xrange(c, M + 1):
            if s * (M + 1) + i not in edge:
                edge[s * (M + 1) + i] = []
            if g * (M + 1) + i not in edge:
                edge[g * (M + 1) + i] = []
            edge[s * (M + 1) + i].append((g * (M + 1) + i - c, c))
            edge[g * (M + 1) + i].append((s * (M + 1) + i - c, c))
    num = N * (M + 1)
    dist = [sys.maxint] * num
    prev = [sys.maxint] * num
    start = A * (M + 1) + M
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while len(q) != 0:
        prov_cost, src = heapq.heappop(q)
        if dist[src] < prov_cost:
            continue
        if src not in edge:
            continue
        for dest, costd in edge[src]:
            if dist[dest] > dist[src] + costd:
                dist[dest] = dist[src] + costd
                heapq.heappush(q, (dist[dest], dest))
                prev[dest] = src
    minCost = sys.maxint
    for i in xrange(M + 1):
        minCost = min(minCost, dist[H * (M + 1) + i])
    if minCost == sys.maxint:
        print "Help!"
    else:
        print minCost