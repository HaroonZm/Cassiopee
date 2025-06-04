n, k = map(int, raw_input().split())
g = []
for _ in xrange(10):
    g.append([])
i = 0
while i < n:
    v, j = map(int, raw_input().split())
    g[j - 1].append(v)
    i += 1
i = 0
while i < 10:
    g[i].sort()
    g[i].reverse()
    i += 1
books = []
for _ in xrange(10):
    books.append([0] * 2005)
i = 0
while i < 10:
    j = 1
    while j <= len(g[i]):
        books[i][j] = books[i][j-1] + g[i][j-1] + 2*(j-1)
        j += 1
    i += 1
dp = []
for _ in xrange(11):
    dp.append([0] * (k + 1))
i = 0
while i < 10:
    j = 1
    while j <= k:
        l = 0
        while l <= j:
            if l < len(books[i]):
                if dp[i][j-l] + books[i][l] > dp[i+1][j]:
                    dp[i+1][j] = dp[i][j-l] + books[i][l]
            l += 1
        j += 1
    i += 1
print(dp[10][k])