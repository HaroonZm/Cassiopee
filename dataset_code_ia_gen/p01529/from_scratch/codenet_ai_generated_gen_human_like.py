import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))

# prefix sums for quick range sum calculation
prefix = [0] * (N + 1)
for i in range(N):
    prefix[i + 1] = prefix[i] + w[i]

# dp[i][j]: minimum cost to cut fish segment from i to j into single pieces, i <= j
dp = [[0] * N for _ in range(N)]

for length in range(2, N + 1):
    for i in range(N - length + 1):
        j = i + length - 1
        cost_sum = prefix[j + 1] - prefix[i]
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + cost_sum
            if cost < dp[i][j]:
                dp[i][j] = cost

print(dp[0][N - 1])