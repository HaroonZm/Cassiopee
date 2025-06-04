n=int(input())
a=[int(input()) for _ in range(n)]
from math import comb
def E(m):
    return m*(m-1)//2
def enough(m):
    edges=E(m)
    total=0
    for x in a:
        total+=E(x)
    return total<=edges
low=max(a)
high=sum(a)
while low<high:
    mid=(low+high)//2
    if enough(mid):
        high=mid
    else:
        low=mid+1
print(low)