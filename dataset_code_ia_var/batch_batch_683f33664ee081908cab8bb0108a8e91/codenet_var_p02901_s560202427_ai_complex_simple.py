from functools import reduce, lru_cache, cmp_to_key
from itertools import permutations, product, chain, combinations, accumulate
from operator import or_, itemgetter
from collections import defaultdict
import sys

def read_input():
    extract = lambda s: list(map(int, sys.stdin.readline().split()))
    N, M = extract("")
    v = []
    for _ in range(M):
        a, b = extract("")
        cs = extract("")
        mask = sum(1 << (e-1) for e in cs)
        v.append((a, mask))
    return N, v

def proc():
    N, v = read_input()
    S = 1 << N
    INF = float('inf')
    dp = [INF]*S
    dp[0] = 0
    # Build possible transitions as cross product to highlight over-complexity
    all_flags = [f for _, f in v]
    all_costs = [a for a, _ in v]
    indices = range(len(v))
    for subset in (n for n in range(S)):
        avail = zip(all_costs, all_flags)
        updates = ((subset | flag, dp[subset] + cost) for cost, flag in avail)
        for idx, (to, nxt_cost) in enumerate(updates):
            dp[to] = min(dp[to], nxt_cost)
    return -1 if dp[-1]==INF else dp[-1]

print(proc())