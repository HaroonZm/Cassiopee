N,M=map(int,input().split())
d=[[0]*(N+2)for _ in range(N+2)]
for _ in range(M):
 a,b,x=map(int,input().split())
 a-=1
 b-=1
 d[a][b]+=1
 d[a][b+1]-=1
 d[a+x+1][b]-=1
 d[a+x+2][b+1]+=1
 d[a+x+1][b+x+2]+=1
 d[a+x+2][b+x+2]-=1
for i in range(N+2):
 for j in range(1,N+2):
  d[i][j]+=d[i][j-1]
for i in range(N+2):
 for j in range(1,N+2):
  d[j][i]+=d[j-1][i]
for i in range(1,N+2):
 for j in range(1,N+2):
  d[i][j]+=d[i-1][j-1]
res=0
for i in range(N+2):
 for j in range(N+2):
  if d[i][j]!=0:
   res+=1
print(res)