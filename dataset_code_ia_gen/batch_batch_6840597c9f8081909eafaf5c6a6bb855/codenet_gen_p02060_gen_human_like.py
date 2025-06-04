N = int(input())
prices = list(map(int, input().split()))
volumes = list(map(int, input().split()))

max_tea = N + max(volumes)  # 少し余裕を持たせた範囲でDP
INF = 10**9
dp = [INF] * (max_tea + 1)
dp[0] = 0

for i in range(max_tea):
    if dp[i] == INF:
        continue
    for p, t in zip(prices, volumes):
        nxt = i + t
        if nxt <= max_tea:
            dp[nxt] = min(dp[nxt], dp[i] + p)

# N人分以上の最小コストを探す
ans = min(dp[N:])
print(ans)