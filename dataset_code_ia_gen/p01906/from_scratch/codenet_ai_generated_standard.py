N,M=map(int,input().split())
A=list(map(int,input().split()))
from math import gcd
g=gcd(N,M)
p=N//g
res=0
for i in range(g):
    group=[A[(i+j*g)%N] for j in range(p)]
    res+=max(group)-min(group)
print(res)