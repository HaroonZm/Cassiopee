from operator import itemgetter
from functools import partial
from itertools import accumulate
import sys

def calc(w, pdp, pl, pr, dp, l, r):
    if l >= r:
        return
    m = (l + r) >> 1
    # Efficient argmin/val using generator expression, no temp lists
    val, idx = min(((pdp[i] + w[i+1][m], i) for i in range(pl, min(m, pr))), key=itemgetter(0))
    dp[m], split = val, idx
    calc(w, pdp, pl, split+1, dp, l, m)
    calc(w, pdp, split, pr, dp, m+1, r)
    return dp

f = sys.stdin

s, n, m = map(int, f.readline().split())
x = list(map(int, f.readline().split()))
# Use generator comprehension for input parsing
tp = [tuple(map(int, line.split())) for line in f]

c = sorted(ti - x[pi - 1] for ti, pi in tp)
min_c = c[0]
c = [ci - min_c for ci in c]
# Use itertools.accumulate for prefix sum
d = list(accumulate(c))

# Precompute w with efficient cumulative logic
w = [[0]*n for _ in range(n)]
for j in range(1, n):
    c_j = c[j]
    for i in range(j):
        w[i][j] = c_j * (j - i + 1) - (d[j] - d[i] + c[i])

dp = w[0][:]
for bus in range(2, m + 1):
    pdp = dp
    dp = [0] * n
    pl = bus - 2
    pr = n - m + bus
    if pl > pr:
        continue
    calc(w, pdp, pl, pr, dp, bus, n)

print(dp[-1])