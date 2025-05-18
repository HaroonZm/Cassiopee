INF=int(1e9)

while 1:
  n,m,p=map(int,input().split())
  if (n,m,p)==(0,0,0): break
  es=[]
  for i in range(m):
    u,v,w=map(int,input().split())
    es.extend([(u,v,w),(v,u,w)])
  
  d=[[INF]*n for _ in range(n)]
  for i in range(n): d[i][i]=0
  for e in es: d[e[0]][e[1]]=e[2]
  for k in range(n):
    for i in range(n):
      for j in range(n):
        d[i][j]=min(d[i][j],d[i][k]+d[k][j])
  
  dp=[[0]*n for _ in range(n)]
  for e in es:
    if d[0][e[0]]+e[2]+d[e[1]][-1]==d[0][-1]:
      dp[e[0]][e[1]]=1
  for k in range(n):
    for i in range(n):
      for j in range(n):
        dp[i][j]+=dp[i][k]*dp[k][j];
  
  for _ in range(p):
    c=int(input())
    print("{:.9f}".format(dp[0][c]*dp[c][-1]/dp[0][-1]))