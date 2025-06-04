n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n):
    u,k,*adj=map(int,input().split())
    graph[u]=adj
dist=[-1]*(n+1)
dist[1]=0
from collections import deque
q=deque([1])
while q:
    u=q.popleft()
    for v in graph[u]:
        if dist[v]<0:
            dist[v]=dist[u]+1
            q.append(v)
for i in range(1,n+1):
    print(i,dist[i])