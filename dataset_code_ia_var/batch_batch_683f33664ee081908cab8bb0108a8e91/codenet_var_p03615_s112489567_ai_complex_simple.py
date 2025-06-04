from itertools import combinations
from functools import reduce
from operator import or_, add
from math import gcd as math_gcd

MOD = 998244353

def D(*x): return int(input()) if len(x)==0 else tuple(map(int,input().split()))
n = D()
P = [D() for _ in range(n)]

E = 0
def norm(a,b):
    if a==0:return complex(0,1)
    if b==0:return complex(1,0)
    g=math_gcd(a,b)
    return complex(a//g,b//g)
for idx,(x,y) in enumerate(P):
    F = set()
    M = {}
    for j in range(idx+1, n):
        dx, dy = P[j][0]-x, P[j][1]-y
        s = norm(dx,dy)
        M[s] = M.get(s,0)+1
    E = (E+reduce(add, map(lambda c: pow(2,c,MOD)-c-1 if c>1 else 0, M.values()),0))%MOD

ans = (pow(2,n,MOD) - E - n*(n-1)//2 - n - 1)%MOD
print(ans)