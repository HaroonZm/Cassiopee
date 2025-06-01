from functools import reduce
from operator import add
n,r,t=map(int,input().split())
speed=list(map(lambda _:int(input()),range(n)))
point=[0]*n
bottle=[0]*r
_=[(lambda i: (point.__setitem__(i,(point[i]+speed[i])%r), bottle.__setitem__(point[i],bottle[point[i]]+1)))(i) for i in range(n)]
def merge_bottle(x,y):return [max(a,b)+b for a,b in zip(x,y)]
def update():
    nonlocal bottle,point
    nums=[0]*r
    for i in range(n):
        bottle[point[i]]-=1
        point[i]=(point[i]+speed[i])%r
        nums[point[i]]+=1
    bottle=merge_bottle(bottle,nums)
for _ in range(t-1): update()
print(reduce(add,bottle))