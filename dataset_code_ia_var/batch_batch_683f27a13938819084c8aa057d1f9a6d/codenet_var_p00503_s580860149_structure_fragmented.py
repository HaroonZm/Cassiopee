import sys
import itertools

def read_input():
    return sys.stdin.read().splitlines()

def parse_first_line(input_lines):
    return [int(x) for x in input_lines[0].split(' ')]

def initialize_grids():
    return set(), set(), set()

def update_grids_with_line(line, x_grid, y_grid, d_grid):
    x1, y1, d1, x2, y2, d2 = [int(x) for x in line.split(' ')]
    add_to_set(x_grid, x1)
    add_to_set(x_grid, x2)
    add_to_set(y_grid, y1)
    add_to_set(y_grid, y2)
    add_to_set(d_grid, d1)
    add_to_set(d_grid, d2)

def add_to_set(grid_set, value):
    grid_set.add(value)

def get_sorted_grids(x_grid, y_grid, d_grid):
    return sorted(x_grid), sorted(y_grid), sorted(d_grid)

def create_grid_indices(sorted_grid):
    return {element: index for index, element in enumerate(sorted_grid)}

def build_all_grid_indices(x_grid, y_grid, d_grid):
    return create_grid_indices(x_grid), create_grid_indices(y_grid), create_grid_indices(d_grid)

def create_3d_fish_dist(x_len, y_len, d_len):
    return [[[0 for _ in range(d_len)] for _ in range(y_len)] for _ in range(x_len)]

def parse_line_to_indices(line, x_grid_index, y_grid_index, d_grid_index):
    x1, y1, d1, x2, y2, d2 = [int(x) for x in line.split(' ')]
    x1_index = x_grid_index[x1]
    x2_index = x_grid_index[x2]
    y1_index = y_grid_index[y1]
    y2_index = y_grid_index[y2]
    d1_index = d_grid_index[d1]
    d2_index = d_grid_index[d2]
    return (x1_index, x2_index, y1_index, y2_index, d1_index, d2_index)

def update_fish_dist(fish_dist, indices_tuple):
    x1_index, x2_index, y1_index, y2_index, d1_index, d2_index = indices_tuple
    for x, y, d in itertools.product(
        range(x1_index, x2_index),
        range(y1_index, y2_index),
        range(d1_index, d2_index)):
        increment_fish_dist(fish_dist, x, y, d)

def increment_fish_dist(fish_dist, x, y, d):
    fish_dist[x][y][d] += 1

def compute_volume(fish_dist, x_grid, y_grid, d_grid, K):
    volume = 0
    for x_index, y_index, d_index in itertools.product(
        range(len(x_grid) - 1), range(len(y_grid) - 1), range(len(d_grid) - 1)):
        if is_cell_at_least_K(fish_dist, x_index, y_index, d_index, K):
            volume += calculate_cell_volume(x_grid, y_grid, d_grid, x_index, y_index, d_index)
    return volume

def is_cell_at_least_K(fish_dist, x_index, y_index, d_index, K):
    return fish_dist[x_index][y_index][d_index] >= K

def calculate_cell_volume(x_grid, y_grid, d_grid, x_index, y_index, d_index):
    x_begin = x_grid[x_index]
    x_end = x_grid[x_index + 1]
    y_begin = y_grid[y_index]
    y_end = y_grid[y_index + 1]
    d_begin = d_grid[d_index]
    d_end = d_grid[d_index + 1]
    return (x_end - x_begin) * (y_end - y_begin) * (d_end - d_begin)

def process_input_and_grids(input_lines):
    N, K = parse_first_line(input_lines)
    x_grid, y_grid, d_grid = initialize_grids()
    for line in input_lines[1:]:
        update_grids_with_line(line, x_grid, y_grid, d_grid)
    x_grid, y_grid, d_grid = get_sorted_grids(x_grid, y_grid, d_grid)
    x_grid_index, y_grid_index, d_grid_index = build_all_grid_indices(x_grid, y_grid, d_grid)
    fish_dist = create_3d_fish_dist(len(x_grid), len(y_grid), len(d_grid))
    for line in input_lines[1:]:
        indices_tuple = parse_line_to_indices(line, x_grid_index, y_grid_index, d_grid_index)
        update_fish_dist(fish_dist, indices_tuple)
    return fish_dist, x_grid, y_grid, d_grid, K

def main():
    input_lines = read_input()
    fish_dist, x_grid, y_grid, d_grid, K = process_input_and_grids(input_lines)
    volume = compute_volume(fish_dist, x_grid, y_grid, d_grid, K)
    print(volume)

main()