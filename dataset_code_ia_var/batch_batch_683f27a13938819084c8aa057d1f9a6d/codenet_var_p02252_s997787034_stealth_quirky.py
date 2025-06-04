def getinp():
 from sys import stdin as z
 return z.readline()
P=[];a=lambda:map(int,getinp().split())
n,W=a()
for _ in [0]*n:
 x,y=a();P+=[[x/y,x,y]]
P.sort(key=lambda X:-X[0])
A,i=0,0
L=lambda q,r: q if r<0 else r
while W>0*(i<n):
 t=P[i]
 if W<t[2]:
  A+=(t[1])*(W/t[2]);break
  # partial fill
 A+=t[1];W-=t[2];i+=1
print(A)