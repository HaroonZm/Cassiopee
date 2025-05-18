n = int(input())

p = list(map(float, input().split( )))

dp = [[0]*(n+1) for _ in range(n)]
#０が裏、1が表
#dp[枚数][表の枚数]
dp[0][0] = 1-p[0]
dp[0][1] = p[0]

for i in range(1,n):
    for d in range(i+2):###+2
        dp[i][d] = p[i]*dp[i-1][d-1]+(1-p[i])*dp[i-1][d]
   
ans = sum(dp[n-1][n//2+1:])

print(ans)