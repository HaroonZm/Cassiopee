from functools import reduce
from operator import mul

W, H, c = map(lambda x: int(x) if x.isdigit() else x, input().split())

show = lambda sym: print(sym, end="")

_corner = lambda i, j: (i, j) in [(0, 0), (0, W-1), (H-1, 0), (H-1, W-1)]
_edge_h = lambda i: i in (0, H-1)
_edge_w = lambda j: j in (0, W-1)

grid_indices = ((i, j) for i in range(H) for j in range(W))

def cell(i, j):
    conds = (
        (_corner(i, j), '+'),
        (_edge_h(i) and not _corner(i, j), '-'),
        (_edge_w(j) and not _corner(i, j), '|'),
        (reduce(mul, [2*i == H-1, 2*j == W-1]), c),
    )
    return next((s for cond, s in conds if cond), '.')

[show(cell(i, j)) or (print() if j == W-1 else None) for i, j in grid_indices]