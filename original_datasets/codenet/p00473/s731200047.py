n = int(input())
dp = [float('inf')]*(n+1)
dp[0] = 0
cost = [int(input()) for _ in range(n-1)]
for i in range(1,n):
    for j in range(i):
        if dp[i-j]+cost[i-1] < dp[j]: dp[j] = dp[i-j]+cost[i-1]# = min(dp[j],dp[i-j]+cost[i-1])
        if dp[j]+cost[i-1] < dp[i-j]: dp[i-j] = dp[j]+cost[i-1]# = min(dp[i-j],dp[j]+cost[i-1])
    #print(dp)
print(dp[n//2])