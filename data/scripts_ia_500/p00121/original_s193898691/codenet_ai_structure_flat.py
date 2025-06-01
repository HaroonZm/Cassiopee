D={}
R=range(8)
D[tuple(R)]=0
SP=[list(R)]
while SP:
 p=SP.pop(0)
 c=D[tuple(p)]
 z=p.index(0)
 for i in range(4):
  dp=0
  if i==0 and z%4<3: dp=1
  elif i==1 and z%4>0: dp=-1
  elif i==2 and z<4: dp=4
  elif i==3 and z>3: dp=-4
  if dp==0: continue
  x=p[:]
  x[z],x[z+dp]=x[z+dp],x[z]
  t=tuple(x)
  if t in D: continue
  SP.append(x)
  D[t]=c+1
import sys
for line in sys.stdin:
 A=map(int,line.split())
 print D[tuple(A)]