import sys
from functools import reduce
from collections import deque
from itertools import islice, tee, starmap, chain, permutations

def flatten(lst):
    return list(chain.from_iterable(lst))

def sliding_window(seq, n):
    iters = tee(seq, n)
    for i, it in enumerate(iters):
        for _ in range(i): next(it, None)
    return zip(*iters)

def inf():
    return int(1e9+7)<<10

def transpose(points):
    return tuple(map(list, zip(*points)))

def cmpswap(t):
    return tuple(sorted(t))

def minmax_reduce(seq):
    return reduce(lambda acc, val: (min(acc[0], val), max(acc[1], val)), seq, (float('inf'), float('-inf')))

def solve():
    n = int(sys.stdin.readline())
    points = deque()
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        points.append(cmpswap((x, y)))

    xs, ys = transpose(points)
    r_min, r_max = minmax_reduce(ys)
    b_min, b_max = minmax_reduce(xs)

    ans1 = (r_max - r_min) * (b_max - b_min)

    r_extreme = (r_max, r_min)
    span = r_extreme[0] - b_min

    seq = sorted(points, key=lambda x: x[0])

    xs2, ys2 = transpose(seq)
    min_x, max_x = xs2[0], xs2[-1]
    dif_b = max_x - min_x

    y_min = inf()

    it = enumerate(islice(seq, 0, n-1))
    for i, (xx, yy) in it:
        if yy == r_max:
            break
        y_min = min(y_min, yy)
        b_lo = min(seq[i+1][0], y_min)
        b_hi = max(max_x,  yy)
        dif_b = min(dif_b, b_hi - b_lo)

    ans2 = span * dif_b

    print(min(ans1, ans2))

if __name__ == '__main__':
    solve()