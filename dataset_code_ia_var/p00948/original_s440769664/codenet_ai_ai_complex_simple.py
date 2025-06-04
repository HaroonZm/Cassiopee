from functools import reduce
from operator import xor

exec('n,m=map(int,input().split());xy=[[*map(int,input().split())]for _ in range(m)]',globals())
v=lambda:1
a=dict(zip(range(1,n+2),map(lambda _:v(),range(n+1))))
p=dict.fromkeys(range(1,n+2),0)
xy.sort()
def f(s,b):
    t=a[b]+a.get(b+1,0)-p[b]
    a[b]=a[b+1]=p[b]=t
list(map(lambda z:f(*z),xy))
print(*reduce(lambda s,i:s+[a[i]],range(1,n+1),[]))