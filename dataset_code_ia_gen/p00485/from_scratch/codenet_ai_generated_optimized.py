import sys
import heapq
input = sys.stdin.readline

N,M,K = map(int,input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,l = map(int,input().split())
    edges[a].append((b,l))
    edges[b].append((a,l))
malls = [int(input()) for _ in range(K)]

INF = 10**15
dist = [INF]*(N+1)
hq = []
for m in malls:
    dist[m] = 0
    heapq.heappush(hq,(0,m))

while hq:
    cd, cv = heapq.heappop(hq)
    if dist[cv]<cd:
        continue
    for nv,nl in edges[cv]:
        nd = cd + nl
        if nd<dist[nv]:
            dist[nv]=nd
            heapq.heappush(hq,(nd,nv))

ans = 0.0
for a in range(1,N+1):
    for b,l in edges[a]:
        if a < b:
            d1 = dist[a]
            d2 = dist[b]
            diff= abs(d1-d2)
            mx = max(d1,d2)
            if diff < l:
                cand = mx + (l - diff)/2
            else:
                cand = mx
            if cand > ans:
                ans = cand

print(round(ans))