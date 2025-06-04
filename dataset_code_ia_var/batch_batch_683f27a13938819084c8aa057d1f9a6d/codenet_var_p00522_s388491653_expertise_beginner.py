INF = 10 ** 20

m, n = map(int, input().split())
manju_lst = []
for i in range(m):
    a = int(input())
    manju_lst.append(a)

manju_lst.sort(reverse=True)

cum_sum = [0]
s = 0
for v in manju_lst:
    s += v
    cum_sum.append(s)

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
        row.append(INF)
    dp.append(row)

for i in range(n):
    dp[i][0] = 0

for x in range(n):
    cx = clst[x]
    ex = elst[x]
    y = m
    while y > 0:
        if y >= cx:
            dp[x][y] = min(dp[x-1][y], dp[x-1][y-cx] + ex)
        else:
            if y+1 <= m:
                dp[x][y] = min(dp[x-1][y], dp[x][y+1])
            else:
                dp[x][y] = min(dp[x-1][y], ex)
        y -= 1

ans = 0
for x in range(m + 1):
    temp = cum_sum[x] - dp[n-1][x]
    if temp > ans:
        ans = temp
print(ans)