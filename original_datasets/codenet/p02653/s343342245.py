MOD = 10 ** 9 + 7
n, a, b = map(int, input().split())

if a > b:
    a, b = b, a

dp_1s = [0] * b
for l in range(a + 2, b):
    dp = [[0, 0] for _ in range(l + 1)] # at i, 0/1 precedes
    dp[1][1] = 1
    for i in range(1, l):
        dp[i + 1][0] = (dp[i + 1][0] + dp[i][0]) % MOD
        dp[i + 1][1] = (dp[i + 1][1] + dp[i][0] + dp[i][1]) % MOD
        if i + a < l:
            dp[i + a][0] = (dp[i + a][0] + dp[i][1]) % MOD
    dp_1s[l] = dp[l][1] - 1

dp_0s_edge = [0] * b
for l in range(a + 1, b):
    dp = [[0, 0] for _ in range(l + 1)]
    dp[a][0] = 1
    for i in range(1, l):
        dp[i + 1][0] = (dp[i + 1][0] + dp[i][0]) % MOD
        dp[i + 1][1] = (dp[i + 1][1] + dp[i][0] + dp[i][1]) % MOD
        if i + a < l:
            dp[i + a][0] = (dp[i + a][0] + dp[i][1]) % MOD
    dp_0s_edge[l] = dp[l][1] 

# starting at i, 0s/1s precede, i.e., 1s/0s follow
# when 0s precede, len of preceding 0s is lt a
dp = [[0, 0] for _ in range(n + 1)]

dp[0] = [1, 1]
# starting with 0s whose len is gt or eq to a
for l in range(a + 1, b):
    dp[l][1] = dp_0s_edge[l]

for i in range(n):
    for j in range(i + 1, min(n + 1, i + b)):
        dp[j][1] = (dp[j][1] + dp[i][0]) % MOD
    for j in range(i + 1, min(n + 1, i + a)):
        dp[j][0] = (dp[j][0] + dp[i][1]) % MOD
    for l in range(a + 2, b):
        if i + l <= n:
            dp[i + l][1] = (dp[i + l][1] + dp[i][0] * dp_1s[l]) % MOD

# ending with 0s whose len is gt or eq to a
for l in range(a + 1, b):
    dp[n][0] = (dp[n][0] + dp[n - l][0] * dp_0s_edge[l]) % MOD

print((pow(2, n, MOD) - sum(dp[n])) % MOD)