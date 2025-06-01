from heapq import heappush,pop

INF=10**18
N,M,K=map(int,input().split())
G=[[] for _ in range(N)]
for _ in range(M):
 s,t,c=map(int,input().split())
 s-=1
 t-=1
 G[s].append((t,c))
 G[t].append((s,c))
d=[INF]*N
lst=[int(input())-1 for _ in range(K)]
que=[]
for s in lst:
 d[s]=0
 heappush(que,(0,s))
while que:
 p=pop(que)
 v=p[1]
 if d[v]<p[0]:
  continue
 for e in G[v]:
  to,c=e
  nd=d[v]+c
  if d[to]>nd:
   d[to]=nd
   heappush(que,(nd,to))
anss=[]
for i in range(N):
 for e in G[i]:
  to,c=e
  x=d[i]+d[to]+c
  if x%2:
   anss.append(x//2+1)
  else:
   anss.append(x//2)
print(max(anss))