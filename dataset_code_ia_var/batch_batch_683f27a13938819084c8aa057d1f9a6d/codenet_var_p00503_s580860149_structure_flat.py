import sys
import itertools

input_lines = sys.stdin.read().splitlines()
N, K = [int(x) for x in input_lines[0].split(' ')]
x_grid = set()
y_grid = set()
d_grid = set()
for line in input_lines[1:]:
    x1, y1, d1, x2, y2, d2 = [int(x) for x in line.split(' ')]
    x_grid.add(x1)
    x_grid.add(x2)
    y_grid.add(y1)
    y_grid.add(y2)
    d_grid.add(d1)
    d_grid.add(d2)
x_grid = sorted(x_grid)
y_grid = sorted(y_grid)
d_grid = sorted(d_grid)
x_grid_index = {}
for i in range(len(x_grid)):
    x_grid_index[x_grid[i]] = i
y_grid_index = {}
for i in range(len(y_grid)):
    y_grid_index[y_grid[i]] = i
d_grid_index = {}
for i in range(len(d_grid)):
    d_grid_index[d_grid[i]] = i
fish_dist = []
for i in range(len(x_grid)):
    layer = []
    for j in range(len(y_grid)):
        layer.append([0]*len(d_grid))
    fish_dist.append(layer)
for line in input_lines[1:]:
    parts = line.split(' ')
    x1 = int(parts[0])
    y1 = int(parts[1])
    d1 = int(parts[2])
    x2 = int(parts[3])
    y2 = int(parts[4])
    d2 = int(parts[5])
    x1_index = x_grid_index[x1]
    x2_index = x_grid_index[x2]
    y1_index = y_grid_index[y1]
    y2_index = y_grid_index[y2]
    d1_index = d_grid_index[d1]
    d2_index = d_grid_index[d2]
    for x in range(x1_index, x2_index):
        for y in range(y1_index, y2_index):
            for d in range(d1_index, d2_index):
                fish_dist[x][y][d] += 1
volume = 0
for x_index in range(len(x_grid)-1):
    for y_index in range(len(y_grid)-1):
        for d_index in range(len(d_grid)-1):
            if fish_dist[x_index][y_index][d_index] >= K:
                x_begin = x_grid[x_index]
                y_begin = y_grid[y_index]
                d_begin = d_grid[d_index]
                x_end = x_grid[x_index + 1]
                y_end = y_grid[y_index + 1]
                d_end = d_grid[d_index + 1]
                volume += (x_end - x_begin) * (y_end - y_begin) * (d_end - d_begin)
print(volume)