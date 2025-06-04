D, N = map(int, input().split())
T = [int(input()) for _ in range(D)]
clothes = [tuple(map(int, input().split())) for _ in range(N)]
suitable = [[j for j, (a, b, c) in enumerate(clothes) if a <= T[i] <= b] for i in range(D)]
dp = [[0]*N for _ in range(D)]
for j in suitable[0]:
    dp[0][j] = 0
for i in range(1, D):
    for j in suitable[i]:
        max_val = 0
        cj = clothes[j][2]
        for k in suitable[i-1]:
            val = dp[i-1][k] + abs(clothes[k][2] - cj)
            if val > max_val:
                max_val = val
        dp[i][j] = max_val
print(max(dp[D-1][j] for j in suitable[D-1]))