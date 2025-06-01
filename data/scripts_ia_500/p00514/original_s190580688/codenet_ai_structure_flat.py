n,m,r=map(int,input().split())
r-=m*n
if r<0:
 print(0)
else:
 a=1
 i=0
 while i<r:
  a*=i+n
  i+=1
 i=0
 while i<r:
  a//=i+1
  i+=1
 print(a)