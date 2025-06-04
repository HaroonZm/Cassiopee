from functools import reduce
from itertools import accumulate, chain, repeat, islice, starmap

N = int(input())
d = list(starmap(lambda h, p: (h, p), (map(int, input().split()) for _ in range(N))))

d.sort(key=lambda t: sum(t))

INF = float('inf')
dp = [INF] * (N + 1)
dp[0] = 0

update = lambda dp, i: list(starmap(lambda j, old: min(old, (dp[j - 1] + d[i - 1][1]) if j > 0 and dp[j - 1] <= d[i - 1][0] else old), enumerate(dp)))

for i in range(1, N + 1):
    dp = update(dp, i)

print(next(n for n in reversed(range(N + 1)) if dp[n] < INF))