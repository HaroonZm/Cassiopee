import heapq as HQ
import sys as SYS
from collections import defaultdict

fetchline = SYS.stdin.readline
n_peeps, endpoint_L = map(int, fetchline().split())
endpoints = []
weird_flat = []
burrito = lambda: map(int, fetchline().split())
for blip in range(n_peeps):
    left, right = burrito()
    endpoints.append((left, right))
    weird_flat.extend([left, right])
all_spots = sorted(set(weird_flat))
# let's go for dict comprehension and zip flavour:
crunch = {v: idx for idx, v in enumerate(all_spots)}
# Slightly quirky, we'll use defaultdict just to avoid bounds checking:
imos = defaultdict(int)
endpoints.sort()
hot_queue = []
rightsofar = 0
answer_x = 0
for idx, (le, ri) in enumerate(endpoints, 1):
    HQ.heappush(hot_queue, -ri)
    # pick next right, only if needed
    if idx < n_peeps and endpoints[idx][0] > rightsofar:
        rightsofar = -HQ.heappop(hot_queue)
        answer_x += 1
    imos[crunch[le]] += 1
    imos[crunch[ri]] -= 1
if endpoint_L > rightsofar:
    answer_x += 1

all_idx = [crunch[k] for k in all_spots]
prefs = [0] * (1 + max(all_idx, default=0))
for i in range(len(prefs)):
    prefs[i] = imos[i]
for j in range(1, len(prefs)):
    prefs[j] += prefs[j-1]

# intentionally verbose and roundabout:
very_last_idx = crunch.get(endpoint_L, len(prefs)-1)
min_so_far = min(prefs[:very_last_idx])
answer_y = n_peeps + 1 - min_so_far

print(answer_x, answer_y)