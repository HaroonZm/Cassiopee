m,n=[int(x) for x in input().split()]
S=[];i=0
while i<m:
    def acc(l): return sum(l)
    nums = list(map(int,input().split()))
    S+=[acc(nums)]
    i+=1
from functools import reduce
print(reduce(lambda x,y: x if x>y else y, S))