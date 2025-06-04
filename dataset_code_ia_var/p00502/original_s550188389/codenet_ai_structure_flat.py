INF = 10 ** 20
d, n = map(int, input().split())
temp = [int(input()) for _ in range(d)]
temp.insert(0, 0)
alst = []
blst = []
clst = []
for _ in range(n):
    a, b, c = map(int, input().split())
    alst.append(a)
    blst.append(b)
    clst.append(c)
dp = [[0] * n for _ in range(d + 1)]
t1 = temp[1]
for i in range(n):
    if not (alst[i] <= t1 <= blst[i]):
        dp[1][i] = -INF
for i in range(2, d + 1):
    t = temp[i]
    for j in range(n):
        cj = clst[j]
        if alst[j] <= t <= blst[j]:
            m = -INF
            for x in range(n):
                diff = cj - clst[x] if cj >= clst[x] else clst[x] - cj
                val = dp[i - 1][x] + diff
                if val > m:
                    m = val
            dp[i][j] = m
print(max(dp[d]))