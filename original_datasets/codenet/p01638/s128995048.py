from math import  pi,cos,sin
r,_x,_y,n=map(int,input().split())
_m=list(map(int,input().split()))
x,y=_x/r,_y/r
m=sum(_m)
t=[0.0]*(n+1)
_t=0
a=[]
for i in range(n):
    _t+=_m[i]/m*2*pi
    t[i+1]=_t
    a.append(int(( 1 + ((sin(t[i])*y-cos(t[i])*x) + (x*cos(t[i+1])-y*sin(t[i+1])) ) / (t[i+1]-t[i]) )*100))
print(*a)