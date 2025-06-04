dp = []
for _ in range(10):
    row = []
    for _ in range(1001):
        row.append(0)
    dp.append(row)
dp[1][0] = 1
dp[0][0] = 1
now = 1
while now <= 100:
    used = 9
    while used > 0:
        dpu = dp[used]
        dpu_1 = dp[used - 1]
        s = now
        while s < 1001:
            dpu[s] = dpu_1[s - now] + dpu[s]
            s += 1
        used -= 1
    now += 1
while True:
    parts = input().split()
    n = int(parts[0])
    s = int(parts[1])
    if n == 0:
        break
    print(dp[n][s])