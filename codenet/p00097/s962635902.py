m=1001
A=range(9)
d=[[0]*m for i in A]
for i in range(101):
  for j in A[::-1]:
    if j==0: d[j][i]=1
    else:
      for k in range(m-i): d[j][k+i]+=d[j-1][k]
while 1:
  n,s=map(int,raw_input().split())
  if n==s==0: break
  print d[n-1][s]