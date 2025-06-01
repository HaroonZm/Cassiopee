D={}
R=range(8)
def f1(i,p):
  dp=0
  if i==0 and p%4<3: dp=1
  elif i==1 and p%4>0: dp=-1
  elif i==2 and p<4: dp=4
  elif i==3 and p>3: dp=-4
  return dp
  
def f():
  global D
  D={tuple(R):0}
  SP=[R]
  while SP:
    a=SP.pop(0)
    c=D[tuple(a)]
    p=a.index(0)
    for i in range(4):
      dp=f1(i,p)
      if dp==0: continue
      x=a[:]
      x[p],x[p+dp]=x[p+dp],x[p]
      tx=tuple(x)
      if tx in D: continue
      SP.append(x)
      D[tx]=c+1
  return

import sys
f()
A=[]
for x in sys.stdin:
  A=map(int,x.split(" "))
  print D[tuple(A)]