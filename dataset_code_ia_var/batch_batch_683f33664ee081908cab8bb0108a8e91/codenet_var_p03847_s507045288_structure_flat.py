N = int(input())
s = bin(N)[2:]
n = len(s)
dp = []
for i in range(n+1):
    dp.append([0,0,0,0])
dp[0][0] = 1
MOD = int(1e9) + 7
i = 0
while i < n:
    if s[i] == '1':
        b = 1
    else:
        b = 0
    j = 0
    while j < 4:
        k = 0
        while k < 3:
            nj = (j << 1) + b - k
            if nj > 3:
                nj = 3
            if nj >= 0:
                dp[i+1][nj] += dp[i][j]
                if dp[i+1][nj] >= MOD:
                    dp[i+1][nj] -= MOD
            k += 1
        j += 1
    i += 1
res = 0
idx = 0
while idx < 4:
    res += dp[n][idx]
    idx += 1
res %= MOD
print(res)