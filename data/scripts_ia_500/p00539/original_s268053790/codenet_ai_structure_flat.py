from collections import deque
import heapq

n,m,c=map(int,raw_input().split())
g=[[] for _ in xrange(n)]
for i in xrange(m):
    a,b,d=map(int,raw_input().split())
    g[a-1].append([b-1,d])
    g[b-1].append([a-1,d])

color=[0]*n
dis={}
for i in xrange(n):
    dis[i]=float('inf')
dis[0]=0
pq=[]
heapq.heappush(pq,[0,0])
while len(pq)!=0:
    t,u=heapq.heappop(pq)
    color[u]=2
    if dis[u]<t:
        continue
    for v,cost in g[u]:
        if color[v]!=2 and dis[u]+cost<dis[v]:
            dis[v]=dis[u]+cost
            color[v]=1
            heapq.heappush(pq,[dis[v],v])

dis=sorted(dis.items(), key=lambda x:x[1])
totalcost=0
for u in xrange(n):
    for v,cost in g[u]:
        totalcost+=cost
totalcost//=2

ans=float('inf')
visited=[0]*n
for u,x in dis:
    visited[u]=1
    for v,cost in g[u]:
        if visited[v]==1:
            totalcost-=cost
    if totalcost+c*x<ans:
        ans=totalcost+c*x
print ans