x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())

from math import sqrt

d1=sqrt((x2-x3)**2+(y2-y3)**2)
d2=sqrt((x1-x3)**2+(y1-y3)**2)
d3=sqrt((x1-x2)**2+(y1-y2)**2)

l=max(d1,max(d2,d3))

def cos(x,y,z):
    return (y**2+z**2-x**2)/(2*y*z)

c1=cos(d1,d2,d3)
c2=cos(d2,d1,d3)
c3=cos(d3,d2,d1)

c1=sqrt((1+c1)/2)
c2=sqrt((1+c2)/2)
c3=sqrt((1+c3)/2)

ct1=sqrt(1/(1/(c1**2)-1))
ct2=sqrt(1/(1/(c2**2)-1))
ct3=sqrt(1/(1/(c3**2)-1))

r=max(d1/(2+ct2+ct3),max(d2/(2+ct1+ct3),d3/(2+ct2+ct1)))

print(r)