from collections import defaultdict
from itertools import combinations
from typing import Dict, Tuple, List

def d_init():
    # Compute distances efficiently using dict comprehensions and itertools
    for (i, ei), (j, ej) in combinations(D.items(), 2):
        a = abs(ei - ej)
        D[(i, j)] = D[(j, i)] = a

def solve(p: int, v: int, w: float) -> Tuple[float, List[int]]:
    if v == (1 << n) - 1:
        return 0, N[p][:]
    if (p, v) in memo:
        return memo[(p, v)]

    min_cost, best_path = float('inf'), []
    for i in range(n):
        i_mask = 1 << i
        if not (v & i_mask):
            cost, path = solve(i, v | i_mask, w + W[i])
            cost += D[(i, p)] * w
            if cost < min_cost:
                min_cost = cost
                best_path = path
    final_path = N[p][:] + best_path
    memo[(p, v)] = (min_cost, final_path)
    return min_cost, final_path

# Read input data
N: Dict[int, List[int]] = {}
D: Dict[Tuple[int, int], float] = {}
W: Dict[int, float] = {}

n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    N[i] = [a]
    D[i] = b / 2000.0
    W[i] = c * 20

d_init()
memo: Dict[Tuple[int, int], Tuple[float, List[int]]] = {}

min_total = float('inf')
result: List[int] = []
for i in range(n):
    cost, res_path = solve(i, 1 << i, W[i] + 70)
    if cost < min_total:
        min_total = cost
        result = res_path

print(' '.join(map(str, result)))