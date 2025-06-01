D, N = map(int, input().split())
T = [int(input()) for _ in range(D)]
clothes = [tuple(map(int, input().split())) for _ in range(N)]

# For each day, find which clothes are suitable
suitable = []
for i in range(D):
    day_suitable = []
    for j in range(N):
        A, B, C = clothes[j]
        if A <= T[i] <= B:
            day_suitable.append((j, C))
    suitable.append(day_suitable)

# dp[i][j]: maximum sum of absolute differences of flamboyance up to day i,
# if we wear the j-th clothes on day i
dp = [[-1]*N for _ in range(D)]

# Initialize dp for day 0
for j, C in suitable[0]:
    dp[0][j] = 0

for i in range(1, D):
    for j, Cj in suitable[i]:
        max_val = -1
        for k, Ck in suitable[i-1]:
            if dp[i-1][k] == -1:
                continue
            val = dp[i-1][k] + abs(Cj - Ck)
            if val > max_val:
                max_val = val
        dp[i][j] = max_val

answer = max(dp[D-1])
print(answer)