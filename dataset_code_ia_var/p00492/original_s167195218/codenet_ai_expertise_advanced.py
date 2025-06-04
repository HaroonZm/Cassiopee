import sys
from itertools import product, starmap
from operator import itemgetter
from functools import partial

sys.setrecursionlimit(100000)

W, H = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(H)]
dx_even, dx_odd = [1, 1, 1, 0, -1, 0], [0, 1, 0, -1, -1, -1]
dy = [-1, 0, 1, 1, 0, -1]
neighbors = (
    lambda x, y: zip((dx_even, dx_odd)[y & 1], dy)
)

def dfs(stack):
    while stack:
        x, y = stack.pop()
        if m[y][x] != 0:
            continue
        m[y][x] = 2
        stack.extend(
            (tx, ty)
            for xx, yy in neighbors(x, y)
            if 0 <= (tx := x + xx) < W and 0 <= (ty := y + yy) < H and m[ty][tx] == 0
        )

edge_coords = (
    ((x, 0) for x in range(W)),
    ((x, H-1) for x in range(W)),
    ((0, y) for y in range(H)),
    ((W-1, y) for y in range(H))
)

for edge in edge_coords:
    dfs(list(edge))

perimeter = 0
for y, row in enumerate(m):
    for x, cell in enumerate(row):
        if cell == 1:
            for xx, yy in neighbors(x, y):
                tx, ty = x + xx, y + yy
                if not (0 <= tx < W and 0 <= ty < H) or m[ty][tx] == 2:
                    perimeter += 1
print(perimeter)