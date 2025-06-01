n,m,r=map(int,input().split())
r-=n*m
if r<0:
    print(0)
else:
    from math import factorial as f
    a=f(n+r-1)
    b=f(r)
    c=f(n-1)
    print(a//b//c)