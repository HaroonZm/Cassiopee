from functools import lru_cache
from operator import itemgetter

def solve(n, Food, Name):
    N = tuple(range(n))

    @lru_cache(maxsize=None)
    def dfs(placed, w1, w2):
        unplaced = tuple(sorted(set(N) - set(placed)))
        if not unplaced:
            return [(placed, w1, w2)]
        results = []
        for e in unplaced:
            weight, limit = Food[e]
            if w2 + weight > limit:
                continue
            new_placed = placed + (e,)
            res = dfs(new_placed, w1 + weight * (n - len(placed)), w2 + weight)
            results.extend(res)
        if not results and placed:
            return [(placed, w1, w2)]
        return results

    result = dfs((), 0, 0)
    if not result:
        return

    best = min(result, key=itemgetter(1))
    for idx in reversed(best[0]):
        print(Name[idx])

while True:
    try:
        n = int(input())
    except EOFError:
        break
    if n == 0:
        break
    Name = {}
    Food = {}
    for i in range(n):
        vals = input().split()
        Name[i] = vals[0]
        Food[i] = tuple(map(int, vals[1:]))
    solve(n, Food, Name)