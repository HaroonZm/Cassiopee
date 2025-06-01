#D問題
N,M = map(int,input().split())
D = [int(input()) for i in range(N)]
C = [int(input()) for j in range(M)]

inf = float("inf")

dp = [[inf for i in range(N+1)] for j in range(M+1)]
dp[0][0] = 0
for j in range(M):
    dp[j+1] = dp[j][0:N+1]
    for i in range(N):
        if dp[j][i] != inf:
            dp[j+1][i+1] = min(dp[j+1][i+1],dp[j][i]+D[i]*C[j])
    #print(dp)
print(dp[M][N])