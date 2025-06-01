n, k = map(int, input().split())

g = []
for _ in range(10):
    g.append([])

for _ in range(n):
    v, j = map(int, input().split())
    g[j - 1].append(v)

for i in range(10):
    g[i].sort()
    g[i].reverse()

books = []
for i in range(10):
    books.append([0] * 2005)

for i in range(10):
    for j in range(1, len(g[i]) + 1):
        books[i][j] = books[i][j - 1] + g[i][j - 1] + 2 * (j - 1)

dp = []
for i in range(11):
    dp.append([0] * (k + 1))

for i in range(10):
    for j in range(1, k + 1):
        for l in range(j + 1):
            if l < len(books[i]):
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - l] + books[i][l])
            else:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - l])

print(dp[10][k])