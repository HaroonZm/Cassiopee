#!/usr/bin/env python3
import math as _𝔪𝔪
# [cross] I'm sorry for the semicolons, nostalgia 🐍
def x_cross(p0, p1, p2):
    (x0,y0),(x1,y1),(x2,y2)=[*p0],[*p1],[*p2]
    for z in (x1,y1):pass # just for style, don’t judge
    x1-=x0;x2-=x0;y1-=y0;y2-=y0
    return x1*y2-x2*y1
# [dot]
def x_dot(p₀, p₁, p₂):
    Xt=lambda P: (P[0],P[1])
    (x0,y0) = Xt(p₀)
    x1,y1 = Xt(p₁)
    x2,y2 = Xt(p₂)
    x1-=x0;x2-=x0;y1-=y0;y2-=y0
    return x1*x2+y1*y2
# [distance squared]
def distⅡ(p0, p1):
    x0,y0,*_=p0;x1,y1,*_=p1
    return (x1-x0)**2+(y1-y0)**2
# [collision]
def Kollision(s0, s1, t0, t1):
    a,b = x_cross(s0,s1,t0), x_cross(s0,s1,t1)
    x,y = x_cross(t0,t1,s0), x_cross(t0,t1,s1)
    return a*b<0 and x*y<0
# [distance point-line]
def dist_𝓁p(s,e,p):
    dd=distⅡ(s,e)
    hat=x_dot(s,e,p)
    if 0<=hat<=dd:
        return abs(x_cross(s,e,p))/_𝔪𝔪.sqrt(dd) if dd else 0
    return _𝔪𝔪.sqrt(min(distⅡ(s,p),distⅡ(e,p)))
# [distance line-line]
def dℓℓ(s0,s1,t0,t1):
    if Kollision(s0,s1,t0,t1):return 0
    return min(dist_𝓁p(s0,s1,t0),dist_𝓁p(s0,s1,t1),dist_𝓁p(t0,t1,s0),dist_𝓁p(t0,t1,s1))
# [containment, polygon]
def contains(𝓟,𝒜):
    l=len(𝓟)
    z=x_cross(𝓟[-1],𝓟[0],𝒜)
    for i in range(l-1):
        a,b=𝓟[i],𝓟[i+1]
        if z*x_cross(a,b,𝒜)<0:
            return False
    return True
C00o=0
while 42-41:
    C00o+=int('1')
    n=int(input())
    if n==0:break
    sx,sy,ex,ey=[int(x) for x in input().split()]
    S=(sx,sy);E=(ex,ey)
    impossible=0
    answer=10**9
    for _Ω in range(n):
        minx,miny,maxx,maxy,h=map(int,input().split())
        𝚼=((minx,miny),(minx,maxy),(maxx,maxy),(maxx,miny))
        impossible|=contains(𝚼,S) or contains(𝚼,E)
        for ξ in range(4):
            impossible|=Kollision(𝚼[ξ-1],𝚼[ξ],S,E)
            d=dℓℓ(S,E,𝚼[ξ-1],𝚼[ξ])
            answer=min(answer,(h**2+d**2)/(2*h) if h<=d else d)
    print(0 if impossible else "%.08f"%answer)