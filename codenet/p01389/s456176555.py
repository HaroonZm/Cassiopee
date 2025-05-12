INF = 1 << 30
H, W = map(int, raw_input().split())
G = [map(int, list(raw_input())) for _ in xrange(H)]
dp = [[0] * W + [INF] for _ in xrange(H)] + [[0] + [INF] * (W)]
for y in xrange(H):
    for x in xrange(W):
            dp[y][x] = min(dp[y-1][x], dp[y][x-1]) + G[y][x]
print dp[H-1][W-1]