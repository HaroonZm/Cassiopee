M,N=map(int,input().split())
S=input()
T=input()
dp=[[0]*(N+1) for _ in range(M+1)]
res=0
for i in range(M+1):
    for j in range(N+1):
        if i>0:
            dp[i][j]=max(dp[i][j],dp[i-1][j])
        if j>0:
            dp[i][j]=max(dp[i][j],dp[i][j-1])
        if i>0 and j>0:
            if S[i-1]!=T[j-1]:
                val=dp[i-1][j-1]+2
                if val>dp[i][j]:
                    dp[i][j]=val
for i in range(M+1):
    for j in range(N+1):
        if dp[i][j]>0:
            res=max(res,dp[i][j])
if res==0:
    for i in range(M):
        if S[i]=='I':
            res=1
            break
    if res==0:
        for j in range(N):
            if T[j]=='I':
                res=1
                break
print(res)