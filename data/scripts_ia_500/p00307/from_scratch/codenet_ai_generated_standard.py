import sys
input=sys.stdin.readline

M,N=map(int,input().split())
w=[0]*(M+1)
t=[0]*(M+1)
for i in range(1,M+1):
    wi,ti=map(int,input().split())
    w[i],t[i]=wi,ti
c=[0]*(N+1)
b=[0]*(N+1)
for i in range(1,N+1):
    ci,bi=map(int,input().split())
    c[i],b[i]=ci,bi

ws=[0]*(M+1)
ts=[0]*(M+1)
for i in range(1,M+1):
    ws[i]=ws[i-1]+w[i]
    ts[i]=ts[i-1]+t[i]

def can(k):
    if k==0:
        return True
    dp=[False]*(k+1)
    dp[0]=True
    for _ in range(N):
        ndp=[False]*(k+1)
        i=j=0
        for i in range(k+1):
            if not dp[i]:
                continue
            j=max(j,i)
            while j<k and ws[j+1]-ws[i]<=c[_+1] and ts[j+1]-ts[i]<=b[_+1]:
                j+=1
            for x in range(i+1,j+1):
                ndp[x]=True
        dp=ndp
    return dp[k]

l,r=0,M
while l<r:
    mid=(l+r+1)//2
    if can(mid):
        l=mid
    else:
        r=mid-1
print(l)