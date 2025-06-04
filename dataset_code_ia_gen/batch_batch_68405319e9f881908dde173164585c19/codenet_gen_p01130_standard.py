import sys
import heapq

def dijkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        cost, u = heapq.heappop(hq)
        if cost > dist[u]:
            continue
        for v, w in graph[u]:
            nc = cost + w
            if nc < dist[v]:
                dist[v] = nc
                heapq.heappush(hq, (nc, v))
    return dist

for line in sys.stdin:
    n,m,s,g1,g2 = map(int,line.split())
    if n==0 and m==0 and s==0 and g1==0 and g2==0:
        break
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        b1,b2,c = map(int,sys.stdin.readline().split())
        graph[b1].append((b2,c))
    dist = dijkstra(n, graph, s)
    print(dist[g1] + dist[g2])