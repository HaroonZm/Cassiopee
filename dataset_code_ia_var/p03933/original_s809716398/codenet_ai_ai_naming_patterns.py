import sys
import numpy as np

input_buffer = sys.stdin.buffer.read
input_readline = sys.stdin.buffer.readline
input_readlines = sys.stdin.buffer.readlines

num_vertices, target_index = map(int, input_buffer().split())

angle_unit = np.pi / num_vertices

def is_less_than_x(area_threshold):
    indices = np.arange(1, num_vertices - 1)
    sin_a = np.sin(indices * angle_unit)
    cos_a = np.cos(indices * angle_unit)
    temp_value = area_threshold / sin_a - cos_a
    angle_diff = np.arccos(temp_value) / angle_unit
    angle_diff[np.isnan(angle_diff)] = -(num_vertices * 2)
    max_index = np.minimum(num_vertices - indices - 1, (num_vertices - indices + angle_diff) / 2).astype(int)
    min_index = (num_vertices - indices) - max_index
    valid_count = np.maximum(0, max_index - min_index + 1).sum()
    total_combinations = num_vertices * ((num_vertices - 1) * (num_vertices - 2) // 2)
    return total_combinations - valid_count < 3 * target_index

search_left = 0.0
search_right = 4.0
for _ in range(100):
    midpoint = (search_left + search_right) / 2
    if is_less_than_x(midpoint):
        search_left = midpoint
    else:
        search_right = midpoint
print(midpoint)