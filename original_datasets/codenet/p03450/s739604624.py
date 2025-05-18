import sys
n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(m)]
connection=[[] for i in range(n)]
for i in range(m):
  connection[l[i][0]-1].append((l[i][1]-1,l[i][2]))
  connection[l[i][1]-1].append((l[i][0]-1,-l[i][2]))

distance=[-999999999999]*n
visited=[-1]*n

def bfs(v):
  distance[v]=0
  next=[v]
  next2=set()
  visitct=0
  while len(next)!=0 and visitct!=n:
    for i in range(len(next)):
      if visited[next[i]]==-1:
        visited[next[i]]=1
        visitct+=1
        for j in range(len(connection[next[i]])):
          if visited[connection[next[i]][j][0]]==-1:
            distance[connection[next[i]][j][0]]=distance[next[i]]+connection[next[i]][j][1]
            next2.add(connection[next[i]][j][0])
    next=list(next2)
    next2=set()

for i in range(n):
  if distance[i]==-999999999999:
    bfs(i)

for i in range(m):
  if distance[l[i][1]-1]-distance[l[i][0]-1]!=l[i][2]:
    print('No')
    sys.exit()
print('Yes')