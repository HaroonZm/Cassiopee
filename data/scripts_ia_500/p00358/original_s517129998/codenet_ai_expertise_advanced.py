import sys
sys.setrecursionlimit(10_002)

H, N = map(int, input().split())
locate_put = [set(), {0, 1}, {1, 2}, {2, 3}, {0, 1, 2, 3}]
not_jama = [{0, 1, 2, 3} for _ in range(H)]

for _ in range(N):
    x, y = map(int, input().split())
    not_jama[y].discard(x)  # discard is safer if element not present

from functools import lru_cache

@lru_cache(None)
def get_fn(h, way_put):
    if h == 0:
        return 0
    best = 0
    prev_not_jama = not_jama[h - 1]
    curr_not_jama = not_jama[h]
    prev_places = locate_put[way_put]
    for way, place_put in enumerate(locate_put):
        place_can_put = curr_not_jama - (prev_places & prev_not_jama)
        if place_put <= place_can_put:
            score = get_fn(h - 1, way)
            score += (way != 0) + (way == 4)
            best = max(best, score)
    return best

print(get_fn(H - 1, 0))