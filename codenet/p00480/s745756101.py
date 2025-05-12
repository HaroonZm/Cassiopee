N=int(input())
a=list(map(int,input().split()))
d=[[0]*21 for i in[0]*~-N]
d[0][a[0]]=1
for i in range(1,N-1):
 for j in range(21):
  d[i][j]=(21>j+a[i]and d[i-1][j+a[i]])+(0<=j-a[i]and d[i-1][j-a[i]])
print(d[N-2][a[N-1]])