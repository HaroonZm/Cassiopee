n_and_m = input().split()
n = int(n_and_m[0])
m = int(n_and_m[1])
a = []
for i in range(m):
    a.append(int(input()))
dp = []
for i in range(n + 10):
    dp.append(0)
dp[0] = 1
for x in a:
    dp[x] = -1
mod = 1000000007
for i in range(n):
    if dp[i] < 0:
        continue
    if dp[i+1] >= 0:
        dp[i+1] = (dp[i+1] + dp[i]) % mod
    if dp[i+2] >= 0:
        dp[i+2] = (dp[i+2] + dp[i]) % mod
print(dp[n])