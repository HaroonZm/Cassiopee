n, k = map(int, input().split())
g = [[] for _ in range(10)]
for _ in range(n):
    v, j = map(int, input().split())
    g[j-1].append(v)

books = [
    [0] + [sum(g_i[:x]) + 2 * (x - 1) for x in range(1, len(g_i) + 1)]
    for g_i in (sorted(arr, reverse=True) for arr in g)
]

dp = [0] * (k + 1)
for i in range(10):
    ndp = dp[:]
    length = len(books[i])
    for used in range(k + 1):
        for pick in range(min(length, used + 1)):
            val = dp[used - pick] + books[i][pick]
            if val > ndp[used]:
                ndp[used] = val
    dp = ndp

print(dp[k])