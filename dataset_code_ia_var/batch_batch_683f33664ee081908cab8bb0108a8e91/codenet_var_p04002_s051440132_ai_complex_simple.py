from collections import defaultdict
from itertools import product, chain
from functools import reduce
from operator import add

H, W, N = map(int, input().split())

neighbors = list(product([-1, 0, 1], repeat=2))
neighbors.remove((0, 0))
neighbors_with_self = [(dx, dy) for dx, dy in neighbors] + [(0,0)]

coords = [tuple(map(int, input().split())) for _ in range(N)]

def limits(v, mx): return 1 < v < mx

def safe_cells(a, b):
    return filter(
        lambda ab: limits(ab[0], H) and limits(ab[1], W),
        ((a+dx, b+dy) for dx, dy in neighbors_with_self)
    )

D = defaultdict(int)
list(map(lambda ab: list(map(lambda cell: D.__setitem__(cell, D[cell]+1), safe_cells(*ab))), coords))

ans = [0]*10
list(map(lambda v: ans.__setitem__(v, ans[v]+1), D.values()))
total_cells = (H-2)*(W-2)
ans[0] = total_cells - sum(ans[1:])

print('\n'.join(map(str, ans)))