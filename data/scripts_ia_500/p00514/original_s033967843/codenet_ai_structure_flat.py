n,m,r=map(int,input().split())
r-=m*n
if r<0:
 print(0)
else:
 d=1
 for i in range(r):
  d*=i+1
 u=1
 for i in range(r):
  u*=i+n
 print(u//d)