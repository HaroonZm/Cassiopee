import sys
from bisect import bisect_left
from itertools import product
from array import array

input_lines = sys.stdin.read().splitlines()
N, K = map(int, input_lines[0].split())
coords = [list(map(int, line.split())) for line in input_lines[1:]]

x_coords = sorted({x for seg in coords for x in (seg[0], seg[3])})
y_coords = sorted({y for seg in coords for y in (seg[1], seg[4])})
d_coords = sorted({d for seg in coords for d in (seg[2], seg[5])})

x_idx = {v:i for i,v in enumerate(x_coords)}
y_idx = {v:i for i,v in enumerate(y_coords)}
d_idx = {v:i for i,v in enumerate(d_coords)}

# 3D array with zeros, using array of arrays of arrays of ints for memory and speed
x_len, y_len, d_len = len(x_coords), len(y_coords), len(d_coords)
fish_dist = [[[0]*(d_len) for _ in range(y_len)] for __ in range(x_len)]

for x1, y1, d1, x2, y2, d2 in coords:
    for x_i, y_i, d_i in product(
        range(x_idx[x1], x_idx[x2]), range(y_idx[y1], y_idx[y2]), range(d_idx[d1], d_idx[d2])
    ):
        fish_dist[x_i][y_i][d_i] += 1

volume = 0
for x_i, y_i, d_i in product(range(x_len-1), range(y_len-1), range(d_len-1)):
    if fish_dist[x_i][y_i][d_i] >= K:
        volume += (
            (x_coords[x_i+1] - x_coords[x_i])
            * (y_coords[y_i+1] - y_coords[y_i])
            * (d_coords[d_i+1] - d_coords[d_i])
        )
print(volume)