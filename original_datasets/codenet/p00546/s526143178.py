from collections import deque
from heapq import heappop,heappush
inf=float("INF")
dq=[]

n,m,k,s=map(int,input().split())
p,q=map(int,input().split())

c=[0]*k
z_dist=[inf]*n
for i in range(k):
    c[i]=int(input())-1
    z_dist[c[i]]=0
    heappush(dq,(0,c[i]))
    
g=[[] for i in range(m)]
a=[0]*m
b=[0]*m
for j in range(m):
    aj,bj=map(int,input().split())
    g[aj-1].append(bj-1)    
    g[bj-1].append(aj-1) 
    a[j]=aj-1
    b[j]=bj-1
  
cc=[p]*n    
    
while dq:
    total,node=heappop(dq)
    for to in g[node]:
        if z_dist[to]>total+1:
            z_dist[to]=total+1
            heappush(dq,(total+1,to))

for i in range(n):
    if z_dist[i]<=s:
        cc[i]=q

g=[[] for i in range(n)]
for i in range(m):
    if (not a[i] in c) and (not b[i] in c):
        g[a[i]].append((b[i],cc[b[i]]))
        g[b[i]].append((a[i],cc[a[i]]))

hq=[]
rst=0
heappush(hq,(0,rst)) 

dist=[inf]*n
dist[rst]=0
while len(hq)>0:
    dd,state = heappop(hq)
    for v,dv in g[state]:
        if dist[v]>dist[state]+dv:
            dist[v]=dist[state]+dv
            heappush(hq,(dist[v],v))

print(dist[n-1]-cc[n-1])