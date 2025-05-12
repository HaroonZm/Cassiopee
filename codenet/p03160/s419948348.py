#配るDP
#Hの添字は1-indexに変更
n=int(input())
H=[0]+list(map(int,input().split()))
dp=[10**10]*(n+1)
dp[1]=0
for i in range(1,n):
    if i+2<=n:
        dp[i+2]=min(dp[i]+abs(H[i]-H[i+2]), dp[i+2])
    dp[i+1]=min(dp[i]+abs(H[i]-H[i+1]), dp[i+1])
print(dp[n])