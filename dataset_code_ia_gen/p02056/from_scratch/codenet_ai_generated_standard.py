import sys
import heapq
input = sys.stdin.readline

N, M, K = map(int, input().split())
P = list(map(int, input().split()))
c = list(map(int, input().split()))
J = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for _ in range(M):
    u,v,t = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v,t))
    graph[v].append((u,t))

def dijkstra(start):
    dist = [float('inf')] * N
    dist[start] = 0
    hq = [(0,start)]
    while hq:
        cd, u = heapq.heappop(hq)
        if dist[u] < cd:
            continue
        for nx, cost in graph[u]:
            nd = cd + cost
            if dist[nx] > nd:
                dist[nx] = nd
                heapq.heappush(hq,(nd,nx))
    return dist

dist = dijkstra(0)

best = [-10**15] * K
for i in range(N):
    val = P[i] - 2 * dist[i]
    ci = c[i] - 1
    if best[ci] < val:
        best[ci] = val

res = [-10**18] * K
for i in range(N):
    ci = c[i] - 1
    val = best[ci] + J[i]
    if res[ci] < val:
        res[ci] = val

for x in res:
    print(x)