import sys
import heapq
input=sys.stdin.readline
N,M=map(int,input().split())
G=[[] for _ in range(N+1)]
for _ in range(M):
 a,b,c=map(int,input().split())
 G[a].append((b,c))
INF=10**15
dist=[INF]*(N+1)
dist[1]=0
hq=[(0,1)]
while hq:
 t,u=heapq.heappop(hq)
 if dist[u]<t:continue
 for v,c in G[u]:
  nt=max(t,c)
  if dist[v]>nt:
   dist[v]=nt
   heapq.heappush(hq,(nt,v))
if dist[N]==INF:
 print(-1)
else:
 print(dist[N])