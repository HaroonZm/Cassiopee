INF = 10 ** 18
n_m = input().split()
n = int(n_m[0])
m = int(n_m[1])
c = input().split()
for i in range(len(c)):
    c[i] = int(c[i])
dp = []
for i in range(n + 1):
    if i == 0:
        dp.append(0)
    else:
        dp.append(INF)
i = 0
while i < m:
    j = c[i]
    while j <= n:
        if dp[j] > dp[j - c[i]] + 1:
            dp[j] = dp[j - c[i]] + 1
        j += 1
    i += 1
print(dp[n])