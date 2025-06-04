N, K = map(int, input().split())
books = [[] for _ in range(11)]
for _ in range(N):
    c, g = map(int, input().split())
    books[g].append(c)

dp = [-float('inf')] * (K + 1)
dp[0] = 0
for g in range(1, 11):
    books[g].sort(reverse=True)
    m = len(books[g])
    prefix = [0]
    for i, c in enumerate(books[g], 1):
        prefix.append(prefix[i-1] + c + i - 1)
    ndp = [-float('inf')] * (K + 1)
    for j in range(K + 1):
        if dp[j] == -float('inf'):
            continue
        ndp[j] = max(ndp[j], dp[j])
        for t in range(1, min(m, K - j) + 1):
            ndp[j + t] = max(ndp[j + t], dp[j] + prefix[t])
    dp = ndp
print(dp[K])