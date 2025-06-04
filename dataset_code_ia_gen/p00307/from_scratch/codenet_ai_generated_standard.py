import sys
input=sys.stdin.readline

M,N=map(int,input().split())
w=[0]*(M+1)
t=[0]*(M+1)
for i in range(1,M+1):
    W,T=map(int,input().split())
    w[i],t[i]=W,T

c=[0]*(N+1)
b=[0]*(N+1)
for i in range(1,N+1):
    C,B=map(int,input().split())
    c[i],b[i]=C,B

ws=[0]*(M+1)
ts=[0]*(M+1)
for i in range(1,M+1):
    ws[i]=ws[i-1]+w[i]
    ts[i]=ts[i-1]+t[i]

def can(x):
    if x==0:
        return True
    dp=[[-1]*(x+1) for _ in range(N+1)]
    dp[0][0]=0
    for i in range(1,N+1):
        for j in range(x+1):
            if dp[i-1][j]<0:
                continue
            dp[i][j]=max(dp[i][j],dp[i-1][j])
            for k in range(j+1,x+1):
                ws_seg=ws[k]-ws[j]
                ts_seg=ts[k]-ts[j]
                if ws_seg<=c[i] and ts_seg<=b[i]:
                    if dp[i-1][j]==k-1:
                        dp[i][k]=max(dp[i][k],k-1)
                else:
                    break
    return dp[N][x]==x-1

l,r=0,M
while l<r:
    mid=(l+r+1)//2
    if can(mid):
        l=mid
    else:
        r=mid-1
print(l)