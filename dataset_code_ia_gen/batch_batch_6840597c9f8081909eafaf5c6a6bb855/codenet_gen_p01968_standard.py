N=int(input())
a=list(map(int,input().split()))
from collections import deque

dp={1:(0,())} # x_value:(length, sequence)

for _ in range(N):
    ndp={}
    for x,(l,s) in dp.items():
        # Option1: Not take any new formula, keep x
        if x in ndp:
            if (l,s)<ndp[x]:
                ndp[x]=(l,s)
        else:
            ndp[x]=(l,s)
        # Option2: For each formula i, take it and update
    for i,ai in enumerate(a,1):
        for x,(l,s) in dp.items():
            nx=ai*x
            nl=l+1
            ns=s+(i,)
            if nx in ndp:
                if (nl,ns)<ndp[nx]:
                    ndp[nx]=(nl,ns)
            else:
                ndp[nx]=(nl,ns)
    dp=ndp

maxv=max(dp.keys())
length,seq=dp[maxv]
print(length)
for x in seq:
    print(x)