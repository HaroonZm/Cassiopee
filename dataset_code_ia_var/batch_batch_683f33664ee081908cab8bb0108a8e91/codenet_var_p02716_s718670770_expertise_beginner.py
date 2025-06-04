n = int(input())
a = list(map(int, input().split()))
dp = []
for i in range(n + 1):
    dp.append([])
    for j in range(4):
        dp[i].append([-10**15, -10**15])

dp[0][0][0] = 0

for i in range(n):
    for j in range(4):
        for k in range(2):
            if j == 3:
                if dp[i][3][1] > dp[i+1][3][0]:
                    dp[i+1][3][0] = dp[i][3][1]
                if dp[i][3][0] + a[i] > dp[i+1][3][1]:
                    dp[i+1][3][1] = dp[i][3][0] + a[i]
            elif j == 2:
                if dp[i][2][1] > dp[i+1][2][0]:
                    dp[i+1][2][0] = dp[i][2][1]
                if dp[i][2][0] + a[i] > dp[i+1][2][1]:
                    dp[i+1][2][1] = dp[i][2][0] + a[i]
                if dp[i][2][0] > dp[i+1][3][0]:
                    dp[i+1][3][0] = dp[i][2][0]
            elif j == 1:
                if dp[i][1][1] > dp[i+1][1][0]:
                    dp[i+1][1][0] = dp[i][1][1]
                if dp[i][1][0] + a[i] > dp[i+1][1][1]:
                    dp[i+1][1][1] = dp[i][1][0] + a[i]
                if dp[i][1][0] > dp[i+1][2][0]:
                    dp[i+1][2][0] = dp[i][1][0]
            else:
                if dp[i][0][1] > dp[i+1][0][0]:
                    dp[i+1][0][0] = dp[i][0][1]
                if dp[i][0][0] + a[i] > dp[i+1][0][1]:
                    dp[i+1][0][1] = dp[i][0][0] + a[i]
                if dp[i][0][0] > dp[i+1][1][0]:
                    dp[i+1][1][0] = dp[i][0][0]

ans = 0
if n % 2 == 0:
    if max(dp[n][0][0], dp[n][0][1]) > dp[n][1][1]:
        ans = max(dp[n][0][0], dp[n][0][1])
    else:
        ans = dp[n][1][1]
else:
    t = max(dp[n][0][0], dp[n][0][1])
    tt = max(dp[n][1][0], dp[n][1][1])
    if tt > t:
        t = tt
    if dp[n][2][1] > t:
        ans = dp[n][2][1]
    else:
        ans = t

print(ans)