n = int(input())
a = list(map(int, input().split()))
dp = [[[-10**15, -10**15] for i in range(4)] for j in range(n+1)]
#dp = [[[0,0] for i in range(4)] for j in range(n+1)]

dp[0][0][0] = 0

for i in range(n):
    for j in range(4):
        for k in range(2):
            if j == 3:
                dp[i+1][3][0] = max(dp[i][3][1],dp[i+1][3][0])
                dp[i+1][3][1] = max(dp[i][3][0]+a[i],dp[i+1][3][1])
            elif j == 2:
                dp[i+1][2][0] = max(dp[i][2][1],dp[i+1][2][0])
                dp[i+1][2][1] = max(dp[i][2][0]+a[i],dp[i+1][2][1])
                dp[i+1][3][0] = max(dp[i][2][0],dp[i+1][3][0])
            elif j == 1:
                dp[i+1][1][0] = max(dp[i][1][1],dp[i+1][1][0])
                dp[i+1][1][1] = max(dp[i][1][0]+a[i],dp[i+1][1][1])
                dp[i+1][2][0] = max(dp[i][1][0],dp[i+1][2][0])
            else:
                dp[i+1][0][0] = max(dp[i][0][1],dp[i+1][0][0])
                dp[i+1][0][1] = max(dp[i][0][0]+a[i],dp[i+1][0][1])
                dp[i+1][1][0] = max(dp[i][0][0],dp[i+1][1][0])

ans = 0
if n % 2 == 0:
    ans = max(max(dp[n][0]), dp[n][1][1])
else:
    ans = max(max(dp[n][0]), max(dp[n][1]), dp[n][2][1])

print(ans)