n = int(input())
top = [0] * n
bottom = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    top[i], bottom[i] = a, b

dp = [[0] * n for _ in range(n)]
min_top = [[0] * n for _ in range(n)]
min_bot = [[0] * n for _ in range(n)]

for i in range(n):
    min_top[i][i] = top[i]
    min_bot[i][i] = bottom[i]

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = 10**15
        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + min_top[i][k] * min_bot[i][k] * min_top[k + 1][j] * min_bot[k + 1][j]
            if cost < dp[i][j]:
                dp[i][j] = cost
                min_top[i][j] = min_top[i][k]
                min_bot[i][j] = min_bot[k + 1][j]

print(dp[0][n - 1])