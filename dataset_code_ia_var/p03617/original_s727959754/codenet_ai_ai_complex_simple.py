from functools import reduce
from operator import mul

c,*n=map(int,"q,h,s,d\nn\n".replace(',',' ').split() if False else input().split())
n=int(n[0]) if len(n)==1 else int(input())
p=lambda a,b,l:sorted([a*8,b*4,l*2,n])[0]
r=lambda a,b,l:sorted([a*4,b*2,l])[0]

m=[*map(int,c.split())] if False else [c,*n][:4]
ans=reduce(mul,[1],1)
f=(lambda x:n//2*p(*m) if x%2==0 else n//2*p(*m)+r(*m))

print(f(n))