from collections import deque
x,y,z,n,m,s,t=map(int,input().split())
g=[[]for _ in range(x+y+z)]
for i in range(n):
  a,b=map(int,input().split())
  g[a-1].append(b+x-1)
  g[b+x-1].append(a-1)
  if i==s-1:
    p,q=a-1,b+x-1
for j in range(m):
  a,b=map(int, input().split())
  g[a+x-1].append(b+x+y-1)
  g[b+x+y-1].append(a+x-1)
  if j==t-1:
    u,v=a+x-1,b+x+y-1
d=[-2]*(x+y+z)
d[p],d[q]=0,0
q=deque([p,q])
while q:
  p = q.popleft()
  for node in g[p]:
    if d[node]==-2:
      q.append(node)
      d[node]=d[p]+1
print(min(d[u],d[v])+1)