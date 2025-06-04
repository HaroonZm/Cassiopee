from functools import reduce
from operator import xor
from itertools import product, accumulate, chain
import sys

input = lambda: sys.stdin.readline()

h, w = map(int, next(iter([input()])).split())

c = list(map(chr, range(150, 150 + w)))
list(map(lambda x: c.extend(list(x.strip())), (input() for _ in range(h))))
h = h + 1
h2 = pow(h, 2)

res = 0

for j in range(1, w):
    d = [0] * (h2)
    # Compute d with an unnecessarily fancy iterator trick
    _ = list(starmap(
        lambda x, y: d.__setitem__(x * h + y,
                                   d[x * h + y - h - 1] + 1 if c[x * w + j] == c[y * w + j - 1] else d[x * h + y - h - 1]),
        product(range(1, h), repeat=2)
    ))

    dp = [10 ** 10] * h2
    list(map(lambda i: [dp.__setitem__(i, 0), dp.__setitem__(i * h, 0)], range(h)))

    for x, y in product(range(1, h), repeat=2):
        dp[x * h + y] = min(dp[x * h + y - 1], dp[x * h - h + y]) + d[x * h + y]

    res += dp[-1]

print(res)