from functools import reduce
from operator import itemgetter
from math import ceil

import sys

sys.setrecursionlimit(10 ** 8)

get_input = lambda: next(iter(sys.stdin if hasattr(sys.stdin, '__iter__') else [raw_input()]))
to_ints = lambda s: tuple(map(int, s.strip().split()))

n = int(get_input())
H, A, D, S = to_ints(get_input())
ans, ls, adverse, impossible = 0, [], [], False

for _ in (lambda x: map(int, range(x)))(n):
    h, a, d, s = to_ints(get_input())
    adjusted_a = a - D
    if s < S:
        ans -= max(0, adjusted_a)
    if (A <= d) * (adjusted_a > 0):
        impossible = True
    elif adjusted_a > 0:
        eff = A - d
        t = int(ceil(h / float(eff)))
        ls.append((float(t) / adjusted_a, t, adjusted_a))

if impossible:
    print -1
    exit()

ls.sort(key=itemgetter(0))
cum_sum, total = 0, ans
for _, t, a in ls:
    cum_sum = sum([cum_sum, t])
    total = sum([total, cum_sum * a])

print total if total < H else -1