from bisect import bisect_left, bisect_right
from itertools import accumulate
from sys import stdin

INF = float('inf')

w, h = map(int, stdin.readline().split())
n = int(stdin.readline())
points = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
xlst, ylst = zip(*points)

# Pre-sorted and double-lists
sorted_x = sorted(xlst)
sorted_y = sorted(ylst)
doubled_x = sorted_x * 2
doubled_y = sorted_y * 2

# Prefix sums for efficient range calculations (using accumulate from itertools)
cum_x = [0] + list(accumulate(sorted_x))
cum_y = [0] + list(accumulate(sorted_y))
total_x = cum_x[-1]
total_y = cum_y[-1]

cx_candidates = [doubled_x[n - 1], doubled_x[n]]
cy_candidates = [doubled_y[n - 1], doubled_y[n]]

best = (INF, INF, INF)  # (cost, cx, cy)

for xi, yi in points:
    # Choose median candidates for x
    cx = cx_candidates[1] if xi <= cx_candidates[0] else cx_candidates[0]
    cy = cy_candidates[1] if yi <= cy_candidates[0] else cy_candidates[0]

    px = bisect_left(sorted_x, cx)
    py = bisect_left(sorted_y, cy)

    # Efficient sum of |x_i-cx| for all i, exploiting prefix sums and sortedness
    if px:
        left = cx * px - cum_x[px]
        right = (total_x - cum_x[px]) - cx * (n - px)
        x_len = 2 * (left + right) - abs(xi - cx)
    else:
        x_len = 2 * (total_x - cx * n) - abs(xi - cx)
    if py:
        left = cy * py - cum_y[py]
        right = (total_y - cum_y[py]) - cy * (n - py)
        y_len = 2 * (left + right) - abs(yi - cy)
    else:
        y_len = 2 * (total_y - cy * n) - abs(yi - cy)

    tlen = x_len + y_len
    # Choose lex smallest (cx, cy) if costs tie
    best = min(best, (tlen, cx, cy))

print(best[0])
print(f"{best[1]} {best[2]}")