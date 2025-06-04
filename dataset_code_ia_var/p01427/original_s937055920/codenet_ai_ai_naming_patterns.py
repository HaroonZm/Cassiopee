import sys
from collections import defaultdict
from math import atan2

def input_read():
    return sys.stdin.readline()

def output_write(text):
    sys.stdout.write(text)

def calc_gcd(val_a, val_b):
    while val_b:
        val_a, val_b = val_b, val_a % val_b
    return val_a

def main_process():
    height, width = map(int, input_read().split())

    grid_matrix = []
    grid_matrix.append([0] * (width + 2))
    grid_matrix.extend([[0] + list(map(".#".index, input_read().strip())) + [0] for _ in range(height)])
    grid_matrix.append([0] * (width + 2))

    dir_counter = defaultdict(int)
    for idx_row in range(height + 1):
        for idx_col in range(width + 1):
            if grid_matrix[idx_row + 1][idx_col] != grid_matrix[idx_row][idx_col + 1] or grid_matrix[idx_row][idx_col] == grid_matrix[idx_row + 1][idx_col + 1]:
                continue
            val_dir = 1 if grid_matrix[idx_row][idx_col] == grid_matrix[idx_row][idx_col + 1] else -1
            delta_x = idx_col
            delta_y = height - idx_row
            if delta_x == 0:
                dir_counter[(0, 1)] += val_dir
            elif delta_y == 0:
                dir_counter[(1, 0)] += val_dir
            else:
                gcd_value = calc_gcd(delta_x, delta_y)
                norm_x = delta_x // gcd_value
                norm_y = delta_y // gcd_value
                dir_counter[(norm_x, norm_y)] += val_dir

    dir_list = list(dir_counter.items())
    dir_list.sort(key=lambda item: atan2(item[0][1], item[0][0]), reverse=True)

    max_value = 0
    current_value = 1
    for (vec_x, vec_y), count_val in dir_list:
        current_value += count_val
        if current_value > max_value:
            max_value = current_value

    output_write("%d\n" % max_value)

main_process()