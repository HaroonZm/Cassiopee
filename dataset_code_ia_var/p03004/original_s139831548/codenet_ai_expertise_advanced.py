from collections import defaultdict
import sys

def parse():
    N = int(sys.stdin.readline())
    dir_map = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
    x_pairs, y_pairs = [], []
    for _ in range(N):
        x, y, d = sys.stdin.readline().split()
        x, y = int(x), int(y)
        dx, dy = dir_map[d]
        x_pairs.append((x, dx))
        y_pairs.append((y, dy))
    return x_pairs, y_pairs

def extremal_points(pairs):
    result = []
    dic = defaultdict(set)
    for p, d in pairs:
        dic[d].add(p)
    for d in (-1, 0, 1):
        if dic[d]:
            ps = dic[d]
            result.extend([(min(ps), d), (max(ps), d)] if len(ps) > 1 else [(ps.pop(), d)])
    return result

def candidate_times(plist):
    from itertools import combinations
    result = set()
    for (p1, d1), (p2, d2) in combinations(plist, 2):
        if d1 == d2:
            continue
        # The following logic analytically resolves all cases (d1,d2)
        if d1 == -1 and d2 == 0: t = p1 - p2
        elif d1 == -1 and d2 == 1: t = (p1 - p2) / 2
        elif d1 == 0 and d2 == -1: t = p2 - p1
        elif d1 == 0 and d2 == 1: t = p1 - p2
        elif d1 == 1 and d2 == -1: t = (p2 - p1) / 2
        elif d1 == 1 and d2 == 0: t = p2 - p1
        else: continue
        if t > 0:
            result.add(t)
    return result

def position(pair, t):
    p, d = pair
    return p + d * t

def area_at(plist_x, plist_y, t):
    xs = (position(pt, t) for pt in plist_x)
    ys = (position(pt, t) for pt in plist_y)
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    return abs(max_x - min_x) * abs(max_y - min_y)

def main():
    x_pairs, y_pairs = parse()
    ex_x = extremal_points(x_pairs)
    ex_y = extremal_points(y_pairs)
    cand_t = {0}
    cand_t |= candidate_times(ex_x)
    cand_t |= candidate_times(ex_y)
    result = min(area_at(ex_x, ex_y, t) for t in cand_t)
    print(result)

main()