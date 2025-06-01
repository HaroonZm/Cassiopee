#!/usr/bin/env python

from sys import stdin as I
_ = input()

def D(p,q):return((p[0]-q[0])**2+(p[1]-q[1])**2)**.5

for L in I:
    X=list(map(float,L.split()))
    a,b,r,c,d,s=X
    dist=D([a,b],[c,d])
    print((dist>r+s)*0 + (dist+s<r)*2 + (dist+r<s)*-2 or 1)