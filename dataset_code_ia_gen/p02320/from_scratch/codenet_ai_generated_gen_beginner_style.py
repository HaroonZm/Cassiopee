N,W = map(int, input().split())
items = []
for _ in range(N):
    v,w,m = map(int, input().split())
    items.append((v,w,m))

dp = [0]*(W+1)

for v,w,m in items:
    for _ in range(m):
        for weight in range(W, w-1, -1):
            if dp[weight-w] + v > dp[weight]:
                dp[weight] = dp[weight-w] + v

print(dp[W])