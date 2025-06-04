from functools import lru_cache
from operator import itemgetter

n = int(input())
items = [tuple(map(int, input().split())) for _ in range(n)]
ids, dists, weights = zip(*((s, d, v * 20) for s, d, v in items))

INF = float('inf')

@lru_cache(maxsize=None)
def score(rest, pos, total_weight):
    if rest == 0:
        return 0.0, ()
    result = (INF, ())
    bits = (i for i in range(n) if rest & (1 << i))
    for i in bits:
        curr_weight = total_weight + weights[i]
        next_rest = rest ^ (1 << i)
        dist = abs(dists[pos] - dists[i]) / 2000 * total_weight
        temp_score, temp_path = score(next_rest, i, curr_weight)
        current = (temp_score + dist, (i,) + temp_path)
        if current < result:
            result = current
    return result

rest_mask = (1 << n) - 1
best = min((score(rest_mask ^ (1 << i), i, 70) for i in range(n)), key=itemgetter(0))
print(*(ids[i] for i in best[1]))