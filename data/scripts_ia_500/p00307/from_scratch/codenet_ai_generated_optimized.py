import sys
input=sys.stdin.readline

M,N=map(int,input().split())
w=[0]*(M+1)
t=[0]*(M+1)
for i in range(1,M+1):
    wi,ti=map(int,input().split())
    w[i]=wi
    t[i]=ti
c=[0]*(N+1)
b=[0]*(N+1)
for i in range(1,N+1):
    ci,bi=map(int,input().split())
    c[i]=ci
    b[i]=bi

W=[0]*(M+1)
T=[0]*(M+1)
for i in range(1,M+1):
    W[i]=W[i-1]+w[i]
    T[i]=T[i-1]+t[i]

dp=[-1]*(M+1)
dp[0]=0
for _ in range(N):
    ndp=[-1]*(M+1)
    j=0
    for i in range(M+1):
        if dp[i]<0:
            continue
        if ndp[i]<dp[i]:
            ndp[i]=dp[i]
        for x in range(ndp[i]+1,M+1):
            sw=W[x]-W[i]
            st=T[x]-T[i]
            if sw>c[_+1] or st>b[_+1]:
                break
            if ndp[i]<x:
                ndp[i]=x
    dp=ndp

print(dp[M] if dp[M]>=0 else 0)