from itertools import count
from sys import stdin

def knapsack(W, items):
    dp = [0] * (W + 1)
    for v, w in items:
        for i in range(W, w - 1, -1):
            nv = dp[i - w] + v
            if nv > dp[i]:
                dp[i] = nv
    return dp

lines = (line.rstrip() for line in stdin)
get_line = lines.__next__

for case_num in count(1):
    W = get_line()
    if W == '0':
        break
    W = int(W)
    n = int(get_line())
    items = [tuple(map(int, get_line().split(','))) for _ in range(n)]
    dp = knapsack(W, items)
    max_value = dp[W]
    min_weight = next(i for i, v in enumerate(dp) if v == max_value)
    print(f'Case {case_num}:\n{max_value}\n{min_weight}')