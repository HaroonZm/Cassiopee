import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import functools

sys.setrecursionlimit(10 ** 7)

INFINITY_NUMBER = 10 ** 20
EPSILON_FLOAT = 1.0 / 10 ** 13
MODULO_CONSTANT = 10 ** 9 + 7

DIRECTIONS_CARDINAL = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRECTIONS_DIAGONAL_AND_CARDINAL = [
    (-1, 0), (-1, 1), (0, 1), (1, 1),
    (1, 0), (1, -1), (0, -1), (-1, -1)
]

def read_int_list():
    return [int(x) for x in sys.stdin.readline().split()]

def read_int_list_zero_based():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def read_float_list():
    return [float(x) for x in sys.stdin.readline().split()]

def read_string_list():
    return sys.stdin.readline().split()

def read_single_int():
    return int(sys.stdin.readline())

def read_single_float():
    return float(sys.stdin.readline())

def read_line_as_string():
    return input()

def print_flush(output_string):
    return print(output_string, flush=True)

def main():
    result_outputs = []

    def process_triangle(n_rows, mine_value):
        # Build a triangle grid with extra padding for easy indexing
        triangle_grid = (
            [[-1] * (n_rows + 3)] +
            [[-1] + read_int_list() + [-1] * 2 for _ in range(n_rows)] +
            [[-1] * (n_rows + 3)]
        )
        triangle_grid_backup = [row[:] for row in triangle_grid]
        mine_info_dict = collections.defaultdict(int)

        def dfs_traverse_same_value_connected_cells(row_idx, col_idx, value):
            if triangle_grid[row_idx][col_idx] == 0:
                return (0, set([(row_idx, col_idx)]))
            if triangle_grid[row_idx][col_idx] != value:
                return (0, set())
            triangle_grid[row_idx][col_idx] = -1
            cell_count_and_set = [1, set()]
            # Explore 6-connected neighbors (hexagonal)
            for delta_row, delta_col in [
                (-1, -1), (-1, 0), (0, -1),
                (0, 1), (1, 0), (1, 1)
            ]:
                traverse_result = dfs_traverse_same_value_connected_cells(
                    row_idx + delta_row, col_idx + delta_col, value
                )
                cell_count_and_set[0] += traverse_result[0]
                cell_count_and_set[1] |= traverse_result[1]
            return tuple(cell_count_and_set)

        # Mark single-cell mine regions
        for row in range(1, n_rows + 1):
            for col in range(1, row + 1):
                if triangle_grid[row][col] != mine_value:
                    continue
                connected_count, connected_set = dfs_traverse_same_value_connected_cells(
                    row, col, triangle_grid[row][col]
                )
                if len(connected_set) == 1:
                    mine_info_dict[list(connected_set)[0]] = -1

        triangle_grid = triangle_grid_backup
        triangle_grid_backup = [row[:] for row in triangle_grid]

        # Identify isolated zeros surrounded by non-mines
        for row in range(1, n_rows + 1):
            for col in range(1, row + 1):
                if triangle_grid[row][col] != 0:
                    continue
                if (row, col) in mine_info_dict:
                    continue
                all_neighbors_non_mine_and_non_zero = True
                for delta_row, delta_col in [
                    (-1, -1), (-1, 0), (0, -1),
                    (0, 1), (1, 0), (1, 1)
                ]:
                    neighbor = triangle_grid[row + delta_row][col + delta_col]
                    if neighbor in [0, mine_value]:
                        all_neighbors_non_mine_and_non_zero = False
                        break
                if all_neighbors_non_mine_and_non_zero:
                    mine_info_dict[(row, col)] = -1
                else:
                    mine_info_dict[(row, col)] = 0

        cell_related_types = collections.defaultdict(set)
        for row in range(1, n_rows + 1):
            for col in range(1, row + 1):
                if triangle_grid[row][col] != mine_value:
                    continue
                current_cell_value = triangle_grid[row][col]
                sign_factor = -1 if triangle_grid[row][col] == mine_value else 1
                connected_count, connected_set = dfs_traverse_same_value_connected_cells(
                    row, col, triangle_grid[row][col]
                )
                if len(connected_set) > 1:
                    for cell_key in connected_set:
                        cell_related_types[cell_key].add(current_cell_value)
                        mine_info_dict[cell_key] = 0

        triangle_grid = triangle_grid_backup

        for row in range(1, n_rows + 1):
            for col in range(1, row + 1):
                if triangle_grid[row][col] < 1:
                    continue
                current_cell_value = triangle_grid[row][col]
                sign_factor = -1 if triangle_grid[row][col] == mine_value else 1
                connected_count, connected_set = dfs_traverse_same_value_connected_cells(
                    row, col, triangle_grid[row][col]
                )
                if len(connected_set) == 1 and current_cell_value not in cell_related_types[list(connected_set)[0]]:
                    mine_info_dict[list(connected_set)[0]] += connected_count * sign_factor

        if len(mine_info_dict) == 0:
            return 0

        return max(mine_info_dict.values())

    while True:
        triangle_size, mine_type_value = read_int_list()
        if triangle_size == 0 and mine_type_value == 0:
            break
        result_outputs.append(
            process_triangle(triangle_size, mine_type_value)
        )

    return '\n'.join(map(str, result_outputs))

print(main())