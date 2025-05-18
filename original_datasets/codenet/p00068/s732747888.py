import sys
def side(p1,p2):
  global D
  y1,x1=p1
  dy=p2[0]-y1
  dx=p2[1]-x1
  for p3 in D[::-1]:
    if p1==p3 or p2==p3:pass
    elif (p3[1]-x1)*dy-dx*(p3[0]-y1)<0:return 0
  else:return 1

while 1:
  n=input()
  if n==0:break
  D=sorted([list(input()) for i in range(n)])
  p=p1=D[0]
  D1=D[:]
  while True:
    for p2 in D1:
      if p1!=p2 and side(p1,p2):break
    p1=p2
    D1.remove(p2)
    if p2==p:break
  print len(D1)