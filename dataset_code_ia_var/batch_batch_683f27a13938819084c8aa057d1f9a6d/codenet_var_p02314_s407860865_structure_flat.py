N, M = map(int, input().split())
C = list(map(int, input().split()))
INF = float('inf')
dp = [INF] * (N + 1)
dp[0] = 0
i = 0
while i < M:
    c = C[i]
    j = 0
    while j < N + 1:
        if j >= c:
            if dp[j] > dp[j - c] + 1:
                dp[j] = dp[j - c] + 1
        j += 1
    i += 1
print(dp[N])