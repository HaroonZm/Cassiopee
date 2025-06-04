from functools import reduce
from itertools import combinations as cmb

maxes = []
while any(map(lambda x: int(x), (d := input().split()))) :
    n, m = map(int, d)
    a = list(map(int, input().split()))
    def maximal_under_m(pair_sum):
        # Trick: -inf replaced by None, filtered by all(), argmax via max(-inf, val)
        return pair_sum if pair_sum <= m else float('-inf')
    res = reduce(
        lambda acc, val: val if val > acc else acc,
        (maximal_under_m(sum(pair)) for pair in cmb(a, 2)),
        float('-inf')
    )
    maxes.append(-1 if res == float('-inf') else res)

list(map(lambda r: print("NONE" if r == -1 else r), maxes))