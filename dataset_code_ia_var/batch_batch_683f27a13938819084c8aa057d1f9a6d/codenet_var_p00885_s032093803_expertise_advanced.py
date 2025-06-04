from sys import stdin
from itertools import islice, pairwise
from functools import partial

inf = float('inf')
input_iter = iter(stdin.readline, '')

while True:
    try:
        n = int(next(input_iter))
    except StopIteration:
        break
    if n == 0:
        break
    pt = [tuple(map(int, next(input_iter).split())) for _ in range(n)]
    p = (0, *map(lambda x: x[0], pt))
    t = (0, *map(lambda x: x[1], pt))

    dp = [[inf] * 4 for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, 4):
            if (j + 1) * p[i - 1] + p[i] <= t[i] - t[i - 1]:
                dp[i][1] = min(dp[i][1], dp[i - 1][j] + p[i - 1] + p[i])
            if abs(p[i - 1] - p[i]) * j <= t[i] - t[i - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + abs(p[i - 1] - p[i]))
        if min(dp[i]) == inf:
            print(f"NG {i}")
            break
    else:
        for j in range(1, 4):
            dp[n][j] += p[-1]
        print(f"OK {min(dp[n][1:])}")