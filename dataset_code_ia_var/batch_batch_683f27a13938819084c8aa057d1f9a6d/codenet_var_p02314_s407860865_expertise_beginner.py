N, M = input().split()
N = int(N)
M = int(M)
C = input().split()
for i in range(M):
    C[i] = int(C[i])

INF = 10**9
dp = []
for i in range(N+1):
    dp.append(INF)

dp[0] = 0

for i in range(M):
    c = C[i]
    for j in range(c, N+1):
        if dp[j-c] + 1 < dp[j]:
            dp[j] = dp[j-c] + 1

print(dp[N])