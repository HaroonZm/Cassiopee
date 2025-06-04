import sys
import heapq

input = sys.stdin.readline

def dijkstra(start, graph, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        cost, node = heapq.heappop(hq)
        if dist[node] < cost:
            continue
        for nxt, c in graph[node]:
            nd = cost + c
            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(hq, (nd, nxt))
    return dist

while True:
    n,m,s,g1,g2 = map(int, input().split())
    if n==0:
        break
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        b1,b2,c = map(int, input().split())
        graph[b1].append((b2,c))
    dist_s = dijkstra(s, graph, n)
    dist_g1 = dijkstra(g1, graph, n)
    dist_g2 = dijkstra(g2, graph, n)
    res = dist_s[g1] + dist_g1[g2]
    res += min(dist_g2[s], dist_g1[s]) if False else 0  # no backward path needed because problem states source to destinations
    ans = dist_s[g1] + dist_g1[g2] + dist_s[g2]
    print(dist_s[g1] + dist_g1[g2] + dist_s[g2] if dist_s[g1] + dist_g1[g2] + dist_s[g2] < dist_s[g2] + dist_g2[g1] + dist_s[g1] else dist_s[g2] + dist_g2[g1] + dist_s[g1]) if False else print(min(dist_s[g1]+dist_g1[g2]+dist_s[g2], dist_s[g2]+dist_g2[g1]+dist_s[g1]))