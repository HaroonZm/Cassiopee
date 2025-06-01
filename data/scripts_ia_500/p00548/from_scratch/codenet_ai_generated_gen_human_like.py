import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

dp = [float('inf')] * (N + 1)
dp[0] = 0

for i in range(1, N + 1):
    max_a = -1
    min_a = 10**10
    for s in range(1, min(M, i) + 1):
        val = A[i - s]
        if val > max_a:
            max_a = val
        if val < min_a:
            min_a = val
        cost = K + s * (max_a - min_a)
        if dp[i - s] + cost < dp[i]:
            dp[i] = dp[i - s] + cost

print(dp[N])