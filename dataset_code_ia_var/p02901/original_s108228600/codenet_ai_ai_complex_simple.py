from functools import reduce
from itertools import product, chain
N, M = map(int, input().split())
keys = list(chain.from_iterable([(lambda a, c: [(reduce(lambda x, y: x | (1 << (y-1)), c, 0), a)])(int(a), list(map(int, c.split()))) for a, _, c in [input().partition(' ') for _ in range(M)]]))
INF = float('inf')
dp = [INF]*pow(2, N)
dp[0] = 0
for s, i in product(range(1<<N), range(M)):
    mask, cost = keys[i]
    dp[s | mask] = min((lambda x, y: x if x < y else y)(dp[s | mask], dp[s] + cost), dp[s | mask])
print(next(filter(lambda x: x != INF, dp[-1:]), -1))