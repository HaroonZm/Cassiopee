import sys
import heapq
input=sys.stdin.readline

N,M,K=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b,l=map(int,input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))

shopping=list(int(input()) for _ in range(K))

INF=10**15
dist=[INF]*(N+1)
hq=[]
for s in shopping:
    dist[s]=0
    heapq.heappush(hq,(0,s))

while hq:
    cd,u=heapq.heappop(hq)
    if dist[u]<cd:
        continue
    for v,l in graph[u]:
        nd=cd+l
        if dist[v]>nd:
            dist[v]=nd
            heapq.heappush(hq,(nd,v))

ans=0.0
for u in range(1,N+1):
    for v,l in graph[u]:
        if u<v:
            du=dist[u]
            dv=dist[v]
            d=(du+dv+l)/2
            if d>ans:
                ans=d

print(round(ans))