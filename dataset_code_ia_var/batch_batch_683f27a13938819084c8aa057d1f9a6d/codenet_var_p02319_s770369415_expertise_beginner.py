n, W = map(int, input().split())
b = []
for i in range(n):
    b.append(list(map(int, input().split())))

dp = [float("inf")] * 10001
dp[0] = 0

for v, w in b:
    for i in range(10000, -1, -1):
        if i + v <= 10000 and dp[i] + w < dp[i + v]:
            dp[i + v] = dp[i] + w

for i in range(9999, -1, -1):
    if dp[i + 1] < dp[i]:
        dp[i] = dp[i + 1]

ans = 0
for i in range(10001):
    if dp[i] <= W:
        ans = i

print(ans)