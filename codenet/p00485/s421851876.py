import heapq

n,m,K=map(int,raw_input().split())
g=[[] for _ in xrange(n)]
cost=[[10**5]*n for _ in xrange(n)]

for i in xrange(m):
    a,b,l=map(int,raw_input().split())
    a-=1;b-=1
    g[a].append(b)
    g[b].append(a)
    cost[a][b]=l
    cost[b][a]=l

pq=[]
d=[float('inf')]*n
for i in xrange(K):
    c=int(raw_input())-1
    heapq.heappush(pq,[0,c])
    d[c]=0
while len(pq)!=0:
    t,u=heapq.heappop(pq)
    if d[u]<t:
        continue
    for v in g[u]:
        if d[u]+cost[u][v]<d[v]:
            d[v]=d[u]+cost[u][v]
            heapq.heappush(pq,[d[v],v])

ans=0
for i in xrange(n):
    for j in g[i]:
        ans=max(ans,(1+d[i]+d[j]+cost[i][j])/2)
print(ans)