N, M = map(int, input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]

# dp[i][j] := minimal fatigue when after j-th day, JOI is at city i
# Impossible states will be set to a large number
INF = 10**15
dp = [[INF] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0

for day in range(1, M + 1):
    for city in range(N + 1):
        # Wait at current city (no fatigue increase)
        if dp[city][day - 1] != INF:
            if dp[city][day] > dp[city][day - 1]:
                dp[city][day] = dp[city][day - 1]
        # Move from city-1 to city on this day (if possible)
        if city > 0 and dp[city - 1][day - 1] != INF:
            cost = dp[city - 1][day - 1] + D[city - 1] * C[day - 1]
            if dp[city][day] > cost:
                dp[city][day] = cost

# Find minimum fatigue at city N on any day up to M
answer = min(dp[N][1: M + 1])
print(answer)