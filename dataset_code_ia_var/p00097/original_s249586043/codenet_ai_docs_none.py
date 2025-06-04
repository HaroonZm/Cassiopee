dp = [[0 for _ in range(1001)] for _ in range(10)]
dp[1][0] = dp[0][0] = 1
for now in range(1, 101):
    for used in range(9, 0, -1):
        dpu = dp[used]
        dpu_1 = dp[used - 1]
        for s in range(now, 1001):
            dpu[s] = dpu_1[s - now] + dpu[s]
while True:
    n, s = map(int, input().split())
    if not n:
        break
    print(dp[n][s])