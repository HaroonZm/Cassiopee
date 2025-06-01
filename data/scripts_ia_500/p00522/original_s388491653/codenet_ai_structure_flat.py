INF = 10 ** 20
m, n = map(int, input().split())
manju_lst = []
for i in range(m):
    manju_lst.append(int(input()))
manju_lst.sort(reverse=True)
acc = 0
cum_sum = [0]
for manju in manju_lst:
    acc += manju
    cum_sum.append(acc)
clst = []
elst = []
for i in range(n):
    c, e = map(int, input().split())
    clst.append(c)
    elst.append(e)
dp = []
for i in range(n):
    row = []
    for j in range(m + 1):
        if j == 0:
            row.append(0)
        else:
            row.append(INF)
    dp.append(row)
for x in range(n):
    cx = clst[x]
    ex = elst[x]
    for y in range(m, 0, -1):
        if x == 0:
            if y >= cx:
                dp[x][y] = ex
            else:
                if y + 1 <= m:
                    dp[x][y] = dp[x][y + 1]
                else:
                    dp[x][y] = ex
        else:
            if y >= cx:
                dp[x][y] = min(dp[x - 1][y], dp[x - 1][y - cx] + ex)
            else:
                if y + 1 <= m:
                    dp[x][y] = min(dp[x - 1][y], dp[x][y + 1])
                else:
                    dp[x][y] = min(dp[x - 1][y], ex)
ans = -INF
for x in range(m + 1):
    val = cum_sum[x] - dp[n - 1][x]
    if val > ans:
        ans = val
print(ans)