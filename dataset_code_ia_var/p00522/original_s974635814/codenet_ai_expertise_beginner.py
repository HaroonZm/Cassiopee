m, n = map(int, raw_input().split())
p = []
for i in range(m):
    p.append(int(raw_input()))
ce = []
for i in range(n):
    ce.append(list(map(int, raw_input().split())))

dp = []
for i in range(n+1):
    row = []
    for j in range(m+1):
        row.append(float('inf'))
    dp.append(row)

for i in range(n+1):
    dp[i][0] = 0

for i in range(n):
    for j in range(1, m+1):
        if j < ce[i][0]:
            if ce[i][1] < dp[i][j]:
                dp[i+1][j] = ce[i][1]
            else:
                dp[i+1][j] = dp[i][j]
            continue
        a = dp[i][j]
        b = dp[i][j-ce[i][0]] + ce[i][1]
        if a < b:
            dp[i+1][j] = a
        else:
            dp[i+1][j] = b

p.sort()
p = p[::-1]
sump = [0] * (m+1)
for i in range(m):
    sump[i+1] = sump[i] + p[i]

ans = 0
for i in range(1, m+1):
    if sump[i] - dp[n][i] > ans:
        ans = sump[i] - dp[n][i]
print(ans)