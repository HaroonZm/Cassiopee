from sys import stdin
from functools import lru_cache

MAX_N = 300
SQUARES = [i * i for i in range(1, int(MAX_N ** 0.5) + 1)]

@lru_cache(maxsize=None)
def ways(n, idx):
    if n == 0:
        return 1
    if n < 0 or idx == len(SQUARES):
        return 0
    return ways(n, idx + 1) + ways(n - SQUARES[idx], idx)

precomputed = [ways(i, 0) for i in range(MAX_N)]

for line in stdin:
    n = int(line)
    if n == 0:
        break
    print(precomputed[n])