N, W = map(int, raw_input().split())
L = sorted([int(raw_input()) for _ in xrange(N)])
total = sum(L)
dp = [1] + [0] * W
ans = 0 if total > W else 1
for i, w in zip(xrange(N, -1, -1), L[::-1]):
    total -= w
    res = W - total
    if res >= 0:
        ans = (ans + sum(dp[max(0, res - w + 1):res + 1])) % (10**9 + 7)
    for j in xrange(W, w - 1, -1):
        dp[j] += dp[j - w]
print ans