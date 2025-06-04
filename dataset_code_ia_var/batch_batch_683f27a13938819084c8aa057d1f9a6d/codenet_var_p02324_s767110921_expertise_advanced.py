from functools import lru_cache
from itertools import combinations

def warshall_floyd(n, dists):
    dist = [row[:] for row in dists]
    for k in range(n):
        dk = dist[k]
        for i, di in enumerate(dist):
            dik = di[k]
            for j in range(n):
                di[j] = min(di[j], dik + dk[j])
    return dist

def solve(n, links, total_d, odds):
    if not odds: return total_d
    dist = warshall_floyd(n, links)
    idx_map = {v: i for i, v in enumerate(odds)}
    submat = [[dist[u][v] for v in odds] for u in odds]
    size = len(odds)

    @lru_cache(maxsize=None)
    def dp(mask):
        if mask == 0: return 0
        lsb = mask & -mask
        i = (lsb - 1).bit_length()
        min_cost = float('inf')
        mask2 = mask ^ (1 << i)
        for j in range(size):
            if mask2 & (1 << j):
                candidate = submat[i][j] + dp(mask2 ^ (1 << j))
                min_cost = min(min_cost, candidate)
        return min_cost

    full = (1 << size) - 1
    return total_d + dp(full)

v, e = map(int, input().split())
dists = [[float('inf')]*v for _ in range(v)]
for i in range(v): dists[i][i] = 0
odds = [0]*v
total_d = 0
for _ in range(e):
    s, t, d = map(int, input().split())
    if d < dists[s][t]:
        dists[s][t] = dists[t][s] = d
    odds[s] ^= 1
    odds[t] ^= 1
    total_d += d
oddnodes = [i for i, f in enumerate(odds) if f]
print(solve(v, dists, total_d, oddnodes))