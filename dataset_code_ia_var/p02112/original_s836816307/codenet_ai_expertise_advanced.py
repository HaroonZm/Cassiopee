from functools import partial
from itertools import islice, cycle

D = 360
x = [0] * D

n = int(input())
for _ in range(n):
    m, d, v, s = map(int, input().split())
    idx = 30 * (m - 1) + (d - 1)
    v_indices = list(islice(cycle(range(D)), idx, idx + v))
    v_mask = set(v_indices)

    for j in range(D):
        if j in v_mask:
            x[j] = max(x[j], s)
        else:
            # Circular distance
            dist_start = min((j - idx) % D, (idx - j) % D)
            dist_end = min((j - ((idx + v - 1) % D)) % D, (((idx + v - 1) % D) - j) % D)
            x[j] = max(x[j], s - min(dist_start, dist_end))

print(min(x))