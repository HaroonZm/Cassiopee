INF = 10 ** 18
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

dp = []
for i in range(n + 1):
    if i == 0:
        dp.append(-1)
    else:
        dp.append(INF)

for i in range(n):
    x = a[i]
    j = 0
    while j < len(dp) and dp[j] < x:
        j += 1
    dp[j] = x

ans = -1
for i in range(n + 1):
    if dp[i] == INF:
        break
    ans = i

print(ans)