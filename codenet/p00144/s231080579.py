from functools import lru_cache

n=int(input())
router={}
for _ in range(n):
    t=[int(i) for i in input().split(" ")]
    r=t[0]
    k=t[1]
    t=t[2::]
    router[r]=t

def transport(s,g):
    distance=[10**10 for i in range(n+1)]
    distance[s]=0
    next=[s]
    for i in range(1,n+1):
        _next=[]
        for j in next:
            _next+=router[j]
        next=list(set(_next))
        for j in next:
            distance[j]=min(i,distance[j])
    return distance[g]+1

p=int(input())
for _ in range(p):
    s,d,v=[int(i) for i in input().split(" ")]
    t=transport(s,d)
    if t<=v:
        print(t)
    else:
        print("NA")