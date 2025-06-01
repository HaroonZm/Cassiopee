import math as m
def b34nch():
 a=int(input())
 I=0
 while I<a:
  i=input().split()
  xa,ya,ra,xb,yb,rb=map(float,i)
  D1=(xa-xb)*(xa-xb)+(ya-yb)*(ya-yb)
  D2=(ra+rb)*(ra+rb)
  Dr=(ra-rb)*(ra-rb)
  if D1<=D2:
   if Dr>D1:
    print((2 if ra>rb else -2))
   else:print(1)
  else:print(0)
  I+=1
b34nch()