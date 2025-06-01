from copy import deepcopy as dp

def show(o):
 x = 0
 while x<10:
  print(''.join([str(c)+'·' for c in o[x]])[:-1])
  x+=1

def e(o,i,j):
 px=[-1,0,0,1,0]
 py=[0,-1,0,0,1]
 k=0
 while k<5:
  a,b=i+py[k],j+px[k]
  if 0<=a<10 and 0<=b<10:
   o[a][b]=int(not o[a][b])
  k+=1

def f(o,n):
 R=[[0]*10 for _ in range(10)]
 i=0
 while i<10:
  if n>>i&1:
   e(o,0,i)
   R[0][i]=1
  i+=1
 i=1
 while i<10:
  j=0
  while j<10:
   if o[i-1][j]:
    e(o,i,j)
    R[i][j]=1
   j+=1
  i+=1
 if sum(o[9])==0:
  show(R)
  return True
 return False

n=int(raw_input())
_=-1
while _<n-1:
 _+=1
 oo=[map(int,raw_input().split())for __ in range(10)]
 i=0
 while i<1024:
  if f(dp(oo),i):
   break
  i+=1