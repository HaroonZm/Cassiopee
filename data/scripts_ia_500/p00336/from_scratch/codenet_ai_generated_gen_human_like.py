t = input().strip()
b = input().strip()
MOD = 10**9 + 7

dp = [0] * (len(b) + 1)
dp[0] = 1

for char in t:
    for i in range(len(b) - 1, -1, -1):
        if b[i] == char:
            dp[i + 1] = (dp[i + 1] + dp[i]) % MOD

print(dp[len(b)] % MOD)