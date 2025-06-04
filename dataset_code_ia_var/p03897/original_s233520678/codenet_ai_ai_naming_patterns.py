import sys
import numpy as np

def read_single_integer():
    return int(sys.stdin.readline())

def initialize_grid(size):
    return np.zeros((size, size), dtype=np.int8)

def apply_base_patterns(matrix):
    matrix[::2, ::2] = 1
    matrix[1::2, 1::2] = 1

def apply_secondary_patterns(matrix):
    matrix[::6, 1::6] = 1
    matrix[::6, 5::6] = 1
    matrix[2::6, 1::6] = 1
    matrix[2::6, 3::6] = 1
    matrix[4::6, 3::6] = 1
    matrix[4::6, 5::6] = 1

def set_border_ones(matrix):
    matrix[0, :] = 1
    matrix[-1, :] = 1
    matrix[:, 0] = 1
    matrix[:, -1] = 1

def clear_diagonal_patterns(matrix):
    matrix[::2, ::2] = 0
    matrix[1::2, 1::2] = 0

def get_ones_coordinates(matrix):
    return np.where(matrix == 1)

def output_coordinates(x_coords, y_coords):
    print(len(x_coords))
    for x_val, y_val in zip(x_coords, y_coords):
        print(x_val, y_val)

def main():
    grid_size = read_single_integer()
    grid_matrix = initialize_grid(grid_size)
    apply_base_patterns(grid_matrix)
    apply_secondary_patterns(grid_matrix)
    set_border_ones(grid_matrix)
    clear_diagonal_patterns(grid_matrix)
    x_indices, y_indices = get_ones_coordinates(grid_matrix)
    output_coordinates(x_indices, y_indices)

if __name__ == "__main__":
    main()