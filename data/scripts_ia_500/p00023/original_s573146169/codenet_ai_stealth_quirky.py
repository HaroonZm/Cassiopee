import math as m
N=int(raw_input())
i=0
while i<N:
    xa,ya,ra,xb,yb,rb=map(float,raw_input().split())
    r=(m.pow(xa-xb,2)+m.pow(ya-yb,2))**.5
    if ra+rb<r: print(0)
    elif abs(ra-rb)<=r: print(1)
    elif ra-rb>r: print(2)
    else: print(-2)
    i+=1