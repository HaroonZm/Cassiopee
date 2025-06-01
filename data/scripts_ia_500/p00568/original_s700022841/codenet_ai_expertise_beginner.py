H, W = map(int, input().split())
A = []
for _ in range(H):
    row = list(map(int, input().split()))
    A.append(row)

max_len = H * W
dp = []
for h in range(H):
    dp.append([])
    for w in range(W):
        dp[h].append([float('inf')] * max_len)

dp[0][0][0] = 0

for l in range(1, max_len):
    for h in range(H):
        for w in range(W):
            if h + w > l:
                continue
            neighbors = []
            if h > 0:
                neighbors.append((h-1, w))
            if h < H - 1:
                neighbors.append((h+1, w))
            if w > 0:
                neighbors.append((h, w-1))
            if w < W - 1:
                neighbors.append((h, w+1))
            min_cost = float('inf')
            for nh, nw in neighbors:
                cost = A[h][w] * (l - 1) * 2 + A[h][w] + dp[nh][nw][l - 1]
                if cost < min_cost:
                    min_cost = cost
            dp[h][w][l] = min_cost

result = min(dp[H - 1][W - 1])
print(result)