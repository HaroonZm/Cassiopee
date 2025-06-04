from functools import reduce
from itertools import accumulate, product, tee

n, m = map(int, input().split())
colors = ['W', 'B', 'R']

lines = [input() for _ in range(n)]
trans = lambda c: list(map(lambda l: m - l.count(c), lines))
arrays = list(map(trans, colors))

prefix_sums = lambda arr: [0] + list(accumulate(arr))
w_ps, b_ps, r_ps = map(prefix_sums, arrays)

def segsum(ps, l, r):
    return ps[r] - ps[l]

res = min(
    segsum(w_ps, 0, i) + segsum(b_ps, i, j+1) + segsum(r_ps, j+1, n)
    for i, j in product(range(1, n-1), range(1, n-1)) if i <= j
)
print(res)