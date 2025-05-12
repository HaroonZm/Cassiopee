import bisect
import sys
from collections import defaultdict
N,M=map(int,input().split())
A=[int(i) for i in input().split()]
B=[int(i) for i in input().split()]
dd=defaultdict(int)
for a in A:
    dd[a]+=1
for b in B:
    dd[b]+=1
for d,n in dd.items():
    if n>=3:
        print(0)
        sys.exit()
A=sorted(A)
B=sorted(B)
ans=1
mod=10**9+7
for i in range(N*M,0,-1):
    x=bisect.bisect_left(A,i)
    y=bisect.bisect_left(B,i)
    if x>=N or y>=M:
        print(0)
        sys.exit()
    if A[x]==i and B[y]==i:
        #print(i)
        continue
    elif A[x]==i:
        ans*=(M-y)
        ans%=mod
    elif B[y]==i:
        ans*=(N-x)
        ans%=mod
    else:
        ans*=((N-x)*(M-y)-(N*M-i))
        ans%=mod
    #print(x,y,i,ans)
print(ans)