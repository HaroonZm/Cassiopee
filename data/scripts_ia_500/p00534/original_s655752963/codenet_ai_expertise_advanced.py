N, M = map(int, input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]

inf = float('inf')
dp = [inf] * (N + 1)
dp[0] = 0

for c in C:
    new_dp = dp[:]
    for i, val in enumerate(dp[:-1]):
        if val != inf:
            cost = val + D[i] * c
            if cost < new_dp[i + 1]:
                new_dp[i + 1] = cost
    dp = new_dp

print(dp[N])