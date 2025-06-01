from heapq import heappush, heappop
INF = 10**18
N, M, K = map(int,input().split())
G = [[] for _ in range(N)]
d = [INF]*N
for _ in range(M):
 s,t,c=map(int,input().split())
 s-=1
 t-=1
 G[s].append((t,c))
 G[t].append((s,c))
lst = [int(input())-1 for _ in range(K)]
que = []
for s in lst:
 d[s]=0
 heappush(que,(0,s))
while que:
 dist,v = heappop(que)
 if d[v]<dist:
  continue
 for to,cost in G[v]:
  nd = d[v]+cost
  if d[to]>nd:
   d[to]=nd
   heappush(que,(nd,to))
anss = []
for i in range(N):
 for to,cost in G[i]:
  x = d[i]+d[to]+cost
  if x%2:
   anss.append(x//2+1)
  else:
   anss.append(x//2)
print(max(anss))