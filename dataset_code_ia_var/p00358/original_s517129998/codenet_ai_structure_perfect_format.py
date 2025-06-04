import sys

sys.setrecursionlimit(10002)

H, N = [int(i) for i in input().split()]
locate_put = [set(), {0, 1}, {1, 2}, {2, 3}, {0, 1, 2, 3}]
not_jama = [{0, 1, 2, 3} for _ in range(H)]
known_fn = {}

for _ in range(N):
    xi, yi = [int(i) for i in input().split()]
    not_jama[yi].remove(xi)

def get_fn(h, way_put):
    if (h, way_put) in known_fn:
        return known_fn[(h, way_put)]
    if h == 0:
        return 0
    best_count = 0
    for way, place_put in enumerate(locate_put):
        place_can_put = (not_jama[h] - locate_put[way_put]) & not_jama[h - 1]
        if place_put.issubset(place_can_put):
            count = get_fn(h - 1, way)
            if way == 0:
                count += 0
            elif way != 4:
                count += 1
            else:
                count += 2
            if count > best_count:
                best_count = count
    known_fn[(h, way_put)] = best_count
    return best_count

print(get_fn(H - 1, 0))