import sys
input=sys.stdin.readline

N,M=map(int,input().split())
P=list(map(int,input().split()))
A,B,C=[0]*(N),[0]*(N),[0]*(N)
for i in range(1,N):
    a,b,c=map(int,input().split())
    A[i]=a
    B[i]=b
    C[i]=c

# count number of times each train line is used
use=[0]*(N)
for i in range(M-1):
    u,v=P[i],P[i+1]
    if u>v:
        u,v=v,u
    for k in range(u,v):
        use[k]+=1

ans=0
for i in range(1,N):
    if use[i]==0:
        continue
    # cost if buy IC card i: C[i] + B[i]*use[i]
    # cost if no IC card: A[i]*use[i]
    ans+=min(C[i]+B[i]*use[i], A[i]*use[i])
print(ans)