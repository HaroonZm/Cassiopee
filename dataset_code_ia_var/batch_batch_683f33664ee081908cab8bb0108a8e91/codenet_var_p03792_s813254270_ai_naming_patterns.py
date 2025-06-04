import sys
import numpy as np

def set_maximum_recursion_limit(limit_value):
    sys.setrecursionlimit(limit_value)

def read_input():
    buffer_stdin = sys.stdin.buffer
    grid_size = int(buffer_stdin.readline())
    grid_array = np.frombuffer(buffer_stdin.read(), dtype='S1').reshape(grid_size, -1)[:, :grid_size]
    return grid_size, grid_array

def convert_grid_to_bool(grid_array, compare_value):
    return grid_array == compare_value

def is_grid_all_false(grid_bool):
    return (~grid_bool).all()

def compute_row_operations(grid_bool):
    row_false_count = np.sum(~grid_bool, axis=1)
    row_false_count += (~grid_bool).all(axis=0)
    return row_false_count

def compute_column_any_false(grid_bool):
    return np.sum((~grid_bool).any(axis=0))

def main():
    RECURSION_LIMIT_MAXIMUM = 10 ** 7
    set_maximum_recursion_limit(RECURSION_LIMIT_MAXIMUM)
    grid_size, grid_array = read_input()
    grid_bool = convert_grid_to_bool(grid_array, b'#')
    if is_grid_all_false(grid_bool):
        print(-1)
        return
    row_operation_count = compute_row_operations(grid_bool)
    column_any_false_count = compute_column_any_false(grid_bool)
    minimum_operation_count = row_operation_count.min() + column_any_false_count
    print(minimum_operation_count)

main()