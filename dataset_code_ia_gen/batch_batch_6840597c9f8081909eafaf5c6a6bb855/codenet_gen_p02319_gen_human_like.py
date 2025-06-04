N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

# Since weights can be very large but values are limited,
# We use a DP on values approach:
# dp[val] = minimum weight to achieve total value val

max_value = sum(v for v, w in items)
INF = 10**15
dp = [INF] * (max_value + 1)
dp[0] = 0

for v, w in items:
    for val in range(max_value - v, -1, -1):
        if dp[val] + w < dp[val + v]:
            dp[val + v] = dp[val] + w

# Find the maximum value achievable with weight <= W
for val in range(max_value, -1, -1):
    if dp[val] <= W:
        print(val)
        break