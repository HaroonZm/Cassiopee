from itertools import combinations, cycle, takewhile
from functools import reduce

def pairs_sum_leq_m(a, m):
    return (s for s in (sum(p) for p in combinations(a, 2)) if s <= m)

inputs = iter(lambda: raw_input(), '')
for nm in takewhile(lambda t: t != (0,0),
    (tuple(map(int, s.split())) for s in inputs)):
    n, m = nm
    a = list(map(int, next(inputs).split()))
    sums = list(pairs_sum_leq_m(a, m))
    print (['NONE', max(sums)][bool(sums)])