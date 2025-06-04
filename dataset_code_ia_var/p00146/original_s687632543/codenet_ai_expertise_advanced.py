from collections import defaultdict
from functools import lru_cache
from itertools import combinations
import sys

sys.setrecursionlimit(10 ** 7)

def d_init(n):
    A = list(D.items())
    for idx1, (i, e) in enumerate(A):
        for j, f in A[idx1 + 1:]:
            tmp = abs(e - f)
            D[(i, j)] = D[(j, i)] = tmp

@lru_cache(maxsize=None)
def solve(idx, visited, weight):
    if visited == (1 << n) - 1:
        return 0, tuple([name[idx]])
    res_cost = float('inf')
    res_route = ()
    for i in range(n):
        mask = 1 << i
        if not visited & mask:
            cost, route = solve(i, visited | mask, weight + W[i])
            step_cost = D[(i, idx)] / 2000.0 * (weight + 70.0)
            total_cost = cost + step_cost
            if total_cost < res_cost:
                res_cost = total_cost
                res_route = route
                res_idx = i
    full_route = (name[idx],) + res_route
    return res_cost, full_route

# Input
name, D, W = {}, {}, {}
n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    name[i] = a
    D[i] = b
    W[i] = c * 20
d_init(n)

best_cost = float('inf')
best_route = ()
for i in range(n):
    cost, route = solve(i, 1 << i, W[i])
    if cost < best_cost:
        best_cost = cost
        best_route = route

print(*best_route)