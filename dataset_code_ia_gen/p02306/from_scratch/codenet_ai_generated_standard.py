x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
from math import sqrt
a=sqrt((x2 - x3)**2 + (y2 - y3)**2)
b=sqrt((x1 - x3)**2 + (y1 - y3)**2)
c=sqrt((x1 - x2)**2 + (y1 - y2)**2)
p=a+b+c
cx=(a*x1+b*x2+c*x3)/p
cy=(a*y1+b*y2+c*y3)/p
s=0.5*abs(x1*(y2 - y3)+x2*(y3 - y1)+x3*(y1 - y2))
r=2*s/p
print(cx,cy,r)