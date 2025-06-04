import sys
import heapq

def dijkstra(graph, start, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cost, u = heapq.heappop(heap)
        if dist[u] < cost:
            continue
        for v, w in graph[u]:
            nd = cost + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
rev_graph = [[] for _ in range(n+1)]

for _ in range(m):
    line = input().strip().replace(',', ' ').split()
    a,b,c,d = map(int, line)
    graph[a].append((b,c))
    graph[b].append((a,d))

s,g,V,P = map(int, input().strip().split(','))

dist_s = dijkstra(graph, s, n)
dist_g = dijkstra(graph, g, n)

ans = V - P - (dist_s[g] + dist_g[s])
print(ans if ans >= 0 else 0)