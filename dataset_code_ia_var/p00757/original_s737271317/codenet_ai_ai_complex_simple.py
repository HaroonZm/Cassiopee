from functools import reduce
from collections import defaultdict
from itertools import product, accumulate, chain

def main(h, w, s):
    import operator as op
    inp = lambda: list(map(int, input().split()))
    grid = list(map(lambda _: inp(), range(h)))
    # Compute prefix sum using reduce and map with cumulative acrobatics
    prefix = [[0] * (w + 1) for _ in range(h + 1)]
    _ = list(map(lambda t: reduce(lambda r, x: (
            r[0]+[r[0][-1]+x], r[1]+[r[1][-1]+r[0][-1]+x] if r[1] else [0]), 
            grid[t], ([0], [])), range(h)))
    for i, row in enumerate(grid):
        prefix[i + 1][1:] = list(accumulate(row, op.add))
    prefix = [list(accumulate(row, op.add)) for row in ([0] * (w + 1),) + tuple(prefix[1:])]
    for i in range(1, h + 1):
        prefix[i] = list(map(op.add, prefix[i], prefix[i - 1]))
    getsum = lambda l,r,d,u: prefix[u+1][r+1]-prefix[d][r+1]-prefix[u+1][l]+prefix[d][l]
    dp = defaultdict(lambda: (0, -float('inf')))
    allsum = getsum(0, w - 1, 0, h - 1)
    for dh in range(1, h + 1):
        for dw in range(1, w + 1):
            for d, l in product(range(h - dh + 1), range(w - dw + 1)):
                u, r = d + dh - 1, l + dw - 1
                cur = getsum(l, r, d, u)
                v = max(1, max(chain([1], (
                    sum(pair[0] for pair in [dp[(l, m, d, u)], dp[(m + 1, r, d, u)]]) 
                    if min(dp[(l, m, d, u)][1], dp[(m+1, r, d, u)][1]) >= 0 else -1
                    for m in range(l, r)) + (
                    sum(pair[0] for pair in [dp[(l, r, d, m)], dp[(l, r, m + 1, u)]])
                    if min(dp[(l, r, d, m)][1], dp[(l, r, m+1, u)][1]) >= 0 else -1
                    for m in range(d, u)
                ))))
                mx = max(
                    [min(dp[(l, m, d, u)][1], dp[(m + 1, r, d, u)][1])
                     if min(dp[(l, m, d, u)][1], dp[(m + 1, r, d, u)][1]) >= 0 else -float('inf')
                     for m in range(l, r)
                    ] + [
                     min(dp[(l, r, d, m)][1], dp[(l, r, m + 1, u)][1])
                     if min(dp[(l, r, d, m)][1], dp[(l, r, m + 1, u)][1]) >= 0 else -float('inf')
                     for m in range(d, u)
                    ] + [s - (allsum - cur)]
                )
                dp[(l, r, d, u)] = (v, mx)
    print(*dp[(0, w - 1, 0, h - 1)])

if __name__ == '__main__':
    list(map(lambda x: x if x is None else None, iter(lambda: (
        (lambda t: None if t == [0, 0, 0] else main(*t))(
            list(map(int, input().split()))
        )
    ), None)))