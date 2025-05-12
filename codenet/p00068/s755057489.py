import sys
def side(p1, p2, p3):
  y1,x1=p1
  y2,x2=p2
  y3,x3=p3
  return (x3-x1)*(y2-y1)-(x2-x1)*(y3-y1)>0
while 1:
  n=input()
  if n==0:break
  D=sorted([list(input()) for i in range(n)])
  p1=D[0]
  D1=D[:]
  while True:
    c=0
    for p2 in D1:
      if p1==p2:continue
      f=[0,0]
      for p3 in D[::-1]:
        if p1==p3 or p2==p3: continue
        f[side(p1,p2,p3)]+=1
      if f[0]==0:break
    p1=p2
    D1.remove(p2)
    if p2==D[0]:break
  print len(D1)