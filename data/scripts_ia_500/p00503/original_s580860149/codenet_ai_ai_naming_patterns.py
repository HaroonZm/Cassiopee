import sys
import itertools

input_raw_lines = sys.stdin.read().splitlines()
input_params_line = input_raw_lines[0]
num_x_k_values = [int(value) for value in input_params_line.split(' ')]
num_x = num_x_k_values[0]
min_required_k = num_x_k_values[1]

set_x_coordinates = set()
set_y_coordinates = set()
set_d_coordinates = set()

input_data_lines = input_raw_lines[1:]
for data_line in input_data_lines:
    data_values = [int(value) for value in data_line.split(' ')]
    x_start, y_start, d_start, x_stop, y_stop, d_stop = data_values
    set_x_coordinates.add(x_start)
    set_x_coordinates.add(x_stop)
    set_y_coordinates.add(y_start)
    set_y_coordinates.add(y_stop)
    set_d_coordinates.add(d_start)
    set_d_coordinates.add(d_stop)

sorted_x_coordinates = sorted(set_x_coordinates)
sorted_y_coordinates = sorted(set_y_coordinates)
sorted_d_coordinates = sorted(set_d_coordinates)

map_x_coordinate_to_index = {coordinate: index for index, coordinate in enumerate(sorted_x_coordinates)}
map_y_coordinate_to_index = {coordinate: index for index, coordinate in enumerate(sorted_y_coordinates)}
map_d_coordinate_to_index = {coordinate: index for index, coordinate in enumerate(sorted_d_coordinates)}

fish_distribution_grid = [[[0 for _ in range(len(sorted_d_coordinates))] for _ in range(len(sorted_y_coordinates))] for _ in range(len(sorted_x_coordinates))]

for data_line in input_data_lines:
    data_values = [int(value) for value in data_line.split(' ')]
    x_start, y_start, d_start, x_stop, y_stop, d_stop = data_values
    x_start_idx = map_x_coordinate_to_index[x_start]
    x_stop_idx = map_x_coordinate_to_index[x_stop]
    y_start_idx = map_y_coordinate_to_index[y_start]
    y_stop_idx = map_y_coordinate_to_index[y_stop]
    d_start_idx = map_d_coordinate_to_index[d_start]
    d_stop_idx = map_d_coordinate_to_index[d_stop]
    for x_idx, y_idx, d_idx in itertools.product(range(x_start_idx, x_stop_idx), range(y_start_idx, y_stop_idx), range(d_start_idx, d_stop_idx)):
        fish_distribution_grid[x_idx][y_idx][d_idx] += 1

total_volume_accumulated = 0
for x_idx, y_idx, d_idx in itertools.product(range(len(sorted_x_coordinates) - 1), range(len(sorted_y_coordinates) - 1), range(len(sorted_d_coordinates) - 1)):
    if fish_distribution_grid[x_idx][y_idx][d_idx] >= min_required_k:
        x_begin_coord = sorted_x_coordinates[x_idx]
        y_begin_coord = sorted_y_coordinates[y_idx]
        d_begin_coord = sorted_d_coordinates[d_idx]
        x_end_coord = sorted_x_coordinates[x_idx + 1]
        y_end_coord = sorted_y_coordinates[y_idx + 1]
        d_end_coord = sorted_d_coordinates[d_idx + 1]
        volume_section = (x_end_coord - x_begin_coord) * (y_end_coord - y_begin_coord) * (d_end_coord - d_begin_coord)
        total_volume_accumulated += volume_section

print(total_volume_accumulated)