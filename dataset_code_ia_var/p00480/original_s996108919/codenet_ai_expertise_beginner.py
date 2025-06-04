N = int(input())
table = list(map(int, input().split()))

dp = []
for i in range(N-1):
    dp.append([0]*21)

dp[0][table[0]] = 1

for i in range(1, N-1):
    for k in range(21):
        if dp[i-1][k] > 0:
            if k + table[i] <= 20:
                dp[i][k + table[i]] += dp[i-1][k]
            if k - table[i] >= 0:
                dp[i][k - table[i]] += dp[i-1][k]

print(dp[N-2][table[N-1]])