from collections import deque
n,m=map(int,input().split())
a=list(map(int,input().split()))
dist=[-1]*n
q=deque()
for x in a:
    dist[x-1]=0
    q.append(x-1)
while q:
    i=q.popleft()
    for ni in (i-1,i+1):
        if 0<=ni<n and dist[ni]==-1:
            dist[ni]=dist[i]+1
            q.append(ni)
print(max(dist))