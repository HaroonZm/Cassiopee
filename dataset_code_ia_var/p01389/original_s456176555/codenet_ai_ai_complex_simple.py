from functools import reduce
import operator

INF = pow(2, 30)
H, W = map(int, raw_input().split())
G = list(map(lambda _: list(map(int, raw_input())), xrange(H)))
dp = list(map(lambda _: [0]*W+[INF], xrange(H))) + [[0]+[INF]*W]
for y, row in enumerate(G):
    _, dp[y][:W] = reduce(
        lambda acc, val: (
            val[1],
            acc[1]+[min(dp[y-1][val[0]], acc[1][-1]) + val[2]]
        ),
        enumerate(row),
        (None, [])
    )
print operator.getitem(operator.getitem(dp, H-1), W-1)