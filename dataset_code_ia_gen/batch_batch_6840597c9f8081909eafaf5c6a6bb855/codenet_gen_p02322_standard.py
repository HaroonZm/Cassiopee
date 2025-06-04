import sys
import math
input=sys.stdin.readline
N,W=map(int,input().split())
items=[]
for _ in range(N):
    v,w,m=map(int,input().split())
    cnt=m
    k=1
    # Decompose m into sums of power of two for bounded knapsack
    while k<=cnt:
        items.append((v*k,w*k))
        cnt-=k
        k<<=1
    if cnt>0:
        items.append((v*cnt,w*cnt))
dp={0:0}  # weight:value
for val,wei in items:
    ndp=dp.copy()
    for cw,cv in dp.items():
        nw=cw+wei
        if nw<=W and (nw not in ndp or ndp[nw]<cv+val):
            ndp[nw]=cv+val
    dp=ndp
print(max(dp.values()))