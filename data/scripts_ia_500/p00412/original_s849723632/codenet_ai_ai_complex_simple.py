from functools import reduce
from operator import itemgetter

n,m=map(int,input().split())
rane=[list() for _ in range(n)]

def getRane():
    return reduce(lambda acc,x: (x[0],x[1]) if x[1]<acc[1] else acc, enumerate(map(len,rane)), (-1,10**9))[0]

for _ in range(m):
    c,num=map(int,input().split())
    c-=1
    (lambda c,num:(print((lambda l:l[0])(lambda l:l.pop(0))(rane[num-1])),None)[1] if c==0 else rane[(index:=getRane())].append(num))(c+1,num)