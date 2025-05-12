R=range;N,K=map(int,input().split());Q=R(N+1);d=[[0]*2**N for _ in Q];f=[[0]*2**N for _ in Q]
for i in Q:
 for j,c in enumerate(input()):d[i][j]=int(c)
for i in R(1,N+1):
 for j in R(1<<i):
  t=j>>i-1&1;r=0
  while r<i and j>>i-1-r&1==t:r+=1
  f[i][j]=r
for i in Q:
 for k in R(i+1,N+1):
  z=k-i;m=(1<<z)-1
  for j in R(1<<k):
   d[i][j>>z]+=d[k][j];r=f[z][j&m]
   if r!=z:d[k-r][j>>z<<z-r|j&(1<<z-r)-1]+=d[k][j]
 for j in R(1<<i):
  if d[i][j]>=K:I=i;J=j;break
print(''if I==J==0else bin(J)[2:].zfill(I))