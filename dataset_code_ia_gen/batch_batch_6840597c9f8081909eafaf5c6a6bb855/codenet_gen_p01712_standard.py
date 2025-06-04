import sys
input=sys.stdin.readline

N,W,H=map(int,input().split())
candidates=[0]*(W+1)
for _ in range(N):
    x,y,w=map(int,input().split())
    l=max(0,x-w)
    r=min(W,x+w)
    for i in range(l,r+1):
        d=abs(x - i)
        l2=max(0,y-(w-d))
        r2=min(H,y+(w-d))
        if candidates[i]<r2:
            candidates[i]=r2
for i in range(W):
    if candidates[i]<candidates[i+1]:
        candidates[i+1]=candidates[i]
for i in range(W-1,-1,-1):
    if candidates[i]<candidates[i+1]:
        candidates[i]=candidates[i+1]
print("Yes" if all(candidates[i]>=H for i in range(W+1)) else "No")