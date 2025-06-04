N, W = map(int, input().split())
weights = [int(input()) for _ in range(N)]

MOD = 1000000007

dp = [0] * (W + 1)
dp[0] = 1  # 空の組み合わせ

for w in weights:
    for j in range(W, w - 1, -1):
        dp[j] = (dp[j] + dp[j - w]) % MOD

result = sum(dp) % MOD
print(result)