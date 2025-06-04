import sys
import heapq
input=sys.stdin.readline
N,M,S,G= map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    u,v,t,c= map(int,input().split())
    graph[u].append((v,t,c))
dist=[float('inf')]*(N+1)
dist[S]=0
hq=[(0,S,0)] # (rain_time, node, time)
while hq:
    r,u,time=heapq.heappop(hq)
    if dist[u]<r:
        continue
    if u==G:
        print(r)
        break
    for v,t,c in graph[u]:
        wait=max(0,t-time)
        nr=r+wait
        ntime=t+c
        if dist[v]>nr:
            dist[v]=nr
            heapq.heappush(hq,(nr,v,ntime))