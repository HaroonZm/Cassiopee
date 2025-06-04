n,x,m=map(int,input().split())
queries=[tuple(map(int,input().split())) for _ in range(m)]
from itertools import product
ans=None
max_sum=-1
for lions in product(range(x+1),repeat=n):
    if all(sum(lions[l-1:r])==s for l,r,s in queries):
        s=sum(lions)
        if s>max_sum:
            max_sum=s
            ans=lions
if ans is None:
    print(-1)
else:
    print(*ans)