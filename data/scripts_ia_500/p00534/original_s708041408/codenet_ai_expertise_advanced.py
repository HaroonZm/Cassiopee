import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = list(map(int, (input() for _ in range(n))))
c = list(map(int, (input() for _ in range(m))))

INF = float('inf')
dp = [INF] * (n + 1)
dp[0] = 0

for cost in c:
    ndp = dp[:]
    for j, val in enumerate(dp[:-1]):
        if val != INF:
            ndp[j + 1] = min(ndp[j + 1], val + cost * d[j])
    dp = ndp

print(dp[n])