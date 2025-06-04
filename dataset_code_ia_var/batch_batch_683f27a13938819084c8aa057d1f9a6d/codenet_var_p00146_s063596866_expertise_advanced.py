from functools import lru_cache, partial
from operator import itemgetter

n = int(input())
D = [tuple(map(int, input().split())) for _ in range(n)]
all_visited = (1 << n) - 1

@lru_cache(maxsize=None)
def dfs(state, pos, w):
    if state == all_visited:
        return 0, ()
    res = None
    d0 = D[pos][1]
    for i, (s, d1, v) in enumerate(D):
        if not (state >> i) & 1:
            cost, order = dfs(state | (1 << i), i, w + 20 * v)
            val = (cost + abs(d0 - d1) * (70 + w), order + (s,))
            if res is None or val < res:
                res = val
    return res

def solve():
    for i, (s0, d0, v0) in enumerate(D):
        cost, order = dfs(1 << i, i, 20 * v0)
        yield cost, order + (s0,)

print(*reversed(min(solve(), key=itemgetter(0))[1]))