from functools import lru_cache
from sys import stdin

def fast_input():
    return map(int, stdin.readline().split())

def normalize_segment(x1, y1, x2, y2):
    return (min(x1, x2) + 1, min(y1, y2) + 1, max(x1, x2) + 1, max(y1, y2) + 1)

def solve():
    gx, gy = fast_input()
    p = int(stdin.readline())
    out = set()
    for _ in range(p):
        x1, y1, x2, y2 = fast_input()
        out.add((normalize_segment(x1, y1, x2, y2)[0:2], normalize_segment(x1, y1, x2, y2)[2:4]))

    @lru_cache(maxsize=None)
    def f(x, y):
        if x < 1 or y < 1:
            return 0
        if (x, y) == (1, 1):
            return 1
        left = ((x-1, y), (x, y))
        up = ((x, y-1), (x, y))
        block_left = left in out
        block_up = up in out
        if block_left and block_up:
            return 0
        if block_left:
            return f(x, y-1)
        if block_up:
            return f(x-1, y)
        return f(x-1, y) + f(x, y-1)

    ans = f(gx+1, gy+1)
    print(ans if ans else "Miserable Hokusai!")
    return 0

n = int(stdin.readline())
for _ in range(n):
    solve()