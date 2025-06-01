N=int(input())
A=list(map(int,input().split()))
W=list(map(int,input().split()))
INF=10**9
l=INF
r=INF
for a,w in zip(A,W):
    if a==1:
        r=min(w,r)
    else:
        l=min(w,l)
if l==INF or r==INF:
    print(0)
else:
    print(l+r)