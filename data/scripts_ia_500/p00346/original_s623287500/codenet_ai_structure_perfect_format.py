from heapq import heappush, heappop
from collections import deque
n,r=map(int,input().split())
G=[[]for _ in range(n)]
for _ in range(r):
 s,t,d=map(int,input().split())
 G[s-1].append((t-1,d))
 G[t-1].append((s-1,d))
INF=10**18
def dijkstra(s):
 dist=[INF]*n
 dist[s]=0
 que=[(0,s)]
 while que:
  cost,s=heappop(que)
  if dist[s]<cost:continue
  for t,d in G[s]:
   if cost+d<dist[t]:
    dist[t]=cost+d
    heappush(que,(cost+d,t))
 ma=max(dist)
 assert ma!=INF
 goal=[i for i in range(n)if dist[i]==ma]
 used=set(goal)
 deq=deque(goal)
 while deq:
  s=deq.popleft()
  for t,d in G[s]:
   if dist[t]+d==dist[s]and t not in used:
    used.add(t)
    deq.append(t)
 return ma,used
A=[dijkstra(s)for s in range(n)]
B=max(ma for ma,_ in A)
ans={i for i in range(n)}
for ma,used in A:
 if ma==B:
  ans-=used
print(len(ans))
for e in sorted(ans):
 print(e+1)