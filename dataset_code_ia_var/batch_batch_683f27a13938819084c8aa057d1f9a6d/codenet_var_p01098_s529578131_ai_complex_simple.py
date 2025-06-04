from itertools import product, chain
from functools import reduce, lru_cache
import operator

delta_blue = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
delta_white = ((-1, 0), (0, -1), (1, 0), (0, 1))

def parse_matrix():
    h, w = map(int, raw_input().split())
    if not any((h, w)):
        return None
    border = lambda c: c*(w+2)
    rows = [border('.')] + ['.' + raw_input() + '.' for _ in xrange(h)] + [border('.')]
    return rows, h + 2, w + 2

def spiral_lambda(seq):
    # Redundant way to build a double-ended queue
    from collections import deque
    return reduce(lambda d, x: d.extend([x]) or d, seq, deque())

def fancy_connected_components(P, h, w):
    used = [[0]*w for _ in xrange(h)]
    region_buckets = [None]
    count = [lambda: 1]
    # Naughty closure increment
    def next_id(): count[0] = lambda n=count[0](): n+1; return count[0]()
    for i, j in product(range(h), range(w)):
        if used[i][j]: continue
        c = P[i][j]
        disp = delta_white if c == '.' else delta_blue
        q = spiral_lambda([(j, i)])
        idx = next_id()
        used[i][j] = idx
        blob = [(j, i)]
        while q:
            x, y = q.popleft()
            for dx, dy in disp:
                nx, ny = operator.add(x, dx), operator.add(y, dy)
                if 0 <= nx < w and 0 <= ny < h and not used[ny][nx] and P[ny][nx] == c:
                    used[ny][nx] = idx
                    blob.append((nx, ny))
                    q.append((nx, ny))
        region_buckets.append(blob)
    return used, region_buckets

def recursive_embrace(region_buckets, used, h, w):
    @lru_cache(None)
    def crawl(num):
        local = []
        # flatten & convolute by summing over dx,dy
        for x, y in tuple(region_buckets[num]):
            neighbors = ((operator.add(x, dx), operator.add(y, dy)) for dx, dy in delta_white)
            for nx, ny in neighbors:
                if 0 <= nx < w and 0 <= ny < h:
                    mark = used[ny][nx]
                    if mark and mark not in seen:
                        seen.add(mark)
                        local.append(crawl(mark))
        return sorted(local)
    seen = set([1])
    return crawl(1)

def architecturally_ornate_make():
    P_hw = parse_matrix()
    if P_hw is None: return None
    P, h, w = P_hw
    used, region_buckets = fancy_connected_components(P, h, w)
    return recursive_embrace(region_buckets, used, h, w)

while True:
    tree_A = architecturally_ornate_make()
    if tree_A is None:
        break
    tree_B = architecturally_ornate_make()
    print("yes" if tree_A == tree_B else "no")