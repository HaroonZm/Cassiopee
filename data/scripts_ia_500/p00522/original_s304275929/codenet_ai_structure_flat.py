INF = 10 ** 20
m, n = map(int, input().split())
manju_lst = [int(input()) for _ in range(m)]
manju_lst.sort(reverse=True)
acc = 0
cum_sum = [0]
for manju in manju_lst:
    acc += manju
    cum_sum.append(acc)
clst = []
elst = []
for _ in range(n):
    c, e = map(int, input().split())
    clst.append(c)
    elst.append(e)
dp = [[INF] * (m + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = 0
for x in range(1, n + 1):
    cx = clst[x - 1]
    ex = elst[x - 1]
    predp = dp[x - 1]
    for y in range(m, 0, -1):
        if y >= cx:
            comp = predp[y - cx] + ex
        elif y + 1 <= m:
            comp = dp[x][y + 1]
        else:
            comp = ex
        dp[x][y] = predp[y] if predp[y] <= comp else comp
dpn = dp[n]
ans = 0
for x in range(m + 1):
    val = cum_sum[x] - dpn[x]
    if val > ans:
        ans = val
print(ans)