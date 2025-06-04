from functools import lru_cache
import sys

sys.setrecursionlimit(10002)

H, N = map(int, input().split())
blocking = [set() for _ in range(H)]
all_pos = frozenset(range(4))

for _ in range(N):
    x, y = map(int, input().split())
    blocking[y].add(x)

allowable = [
    frozenset(),
    frozenset({0, 1}),
    frozenset({1, 2}),
    frozenset({2, 3}),
    frozenset({0, 1, 2, 3})
]

@lru_cache(maxsize=None)
def dp(level, prev_mask):
    if level < 0:
        return 0
    free = all_pos - blocking[level]
    max_cnt = 0
    for put, cur_mask in enumerate(allowable):
        if cur_mask <= free and cur_mask.isdisjoint(allowable[prev_mask]):
            add = 0 if put == 0 else (2 if put == 4 else 1)
            max_cnt = max(max_cnt, dp(level - 1, put) + add)
    return max_cnt

print(dp(H - 1, 0))