from collections import defaultdict
from itertools import product
from sys import stdin

coord_map = {c: divmod(i, 3) for i, c in enumerate('ABCDEFGHI')}
moves = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def readint():
    try:
        return int(next(stdin).strip())
    except (StopIteration, ValueError):
        return 0

while (n := readint()):
    s, t, b = next(stdin).split()
    dp = [defaultdict(int) for _ in range(n + 1)]
    start = coord_map[s]
    block = coord_map[b]
    target = coord_map[t]
    dp[0][start] = 1

    for i in range(n):
        for (y, x), cnt in dp[i].items():
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < 3 and 0 <= ny < 3) or (ny, nx) == block:
                    dp[i + 1][(y, x)] += cnt
                else:
                    dp[i + 1][(ny, nx)] += cnt

    result = dp[n][target] / 4.0 ** n
    print(f"{result:.8f}")