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

GLOBAL_SYS_RECURSION_LIMIT = 10**7
GLOBAL_INF = 10**20
GLOBAL_EPS = 1.0 / 10**13
GLOBAL_MOD = 10**9 + 7
GLOBAL_DIRECTIONS_4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
GLOBAL_DIRECTIONS_8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

sys.setrecursionlimit(GLOBAL_SYS_RECURSION_LIMIT)

def read_int_list(): 
    return [int(element) for element in sys.stdin.readline().split()]

def read_int_list_decremented(): 
    return [int(element) - 1 for element in sys.stdin.readline().split()]

def read_float_list(): 
    return [float(element) for element in sys.stdin.readline().split()]

def read_str_list(): 
    return sys.stdin.readline().split()

def read_int(): 
    return int(sys.stdin.readline())

def read_float(): 
    return float(sys.stdin.readline())

def read_str(): 
    return input()

def print_flush(message): 
    return print(message, flush=True)

def main():
    result_list = []
    pattern_matrix_mapping = []
    for row_index in range(3):
        row_patterns = []
        for col_index in range(3):
            square_indices = [
                row_index * 4 + col_index,
                row_index * 4 + col_index + 1,
                row_index * 4 + col_index + 4,
                row_index * 4 + col_index + 5
            ]
            row_patterns.append(square_indices)
        pattern_matrix_mapping.append(row_patterns)

    def process_grid(num_rows):
        grid_data = [read_int_list() for _ in range(num_rows)]
        failed_state_tracker = set()
        
        def recursive_search(curr_row, curr_col, curr_depth, corner_1_depth, corner_2_depth, corner_3_depth, corner_4_depth):
            if curr_depth >= num_rows:
                return True
            memoization_key = (
                curr_row,
                curr_col,
                curr_depth,
                corner_1_depth,
                corner_2_depth,
                corner_3_depth,
                corner_4_depth
            )
            if memoization_key in failed_state_tracker:
                return False
            if curr_row == 0:
                if curr_col == 0:
                    corner_1_depth = curr_depth
                elif curr_col == 2:
                    corner_2_depth = curr_depth
            elif curr_row == 2:
                if curr_col == 0:
                    corner_3_depth = curr_depth
                elif curr_col == 2:
                    corner_4_depth = curr_depth
            for grid_cell_idx in pattern_matrix_mapping[curr_row][curr_col]:
                if grid_data[curr_depth][grid_cell_idx] > 0:
                    failed_state_tracker.add(memoization_key)
                    return False
            min_corner_depth = min([
                corner_1_depth,
                corner_2_depth,
                corner_3_depth,
                corner_4_depth
            ])
            if curr_depth - min_corner_depth >= 7:
                failed_state_tracker.add(memoization_key)
                return False
            if recursive_search(curr_row, curr_col, curr_depth + 1, corner_1_depth, corner_2_depth, corner_3_depth, corner_4_depth):
                return True
            for next_row in range(3):
                if curr_row == next_row:
                    continue
                if recursive_search(next_row, curr_col, curr_depth + 1, corner_1_depth, corner_2_depth, corner_3_depth, corner_4_depth):
                    return True
            for next_col in range(3):
                if curr_col == next_col:
                    continue
                if recursive_search(curr_row, next_col, curr_depth + 1, corner_1_depth, corner_2_depth, corner_3_depth, corner_4_depth):
                    return True
            failed_state_tracker.add(memoization_key)
            return False

        if recursive_search(1, 1, 0, -1, -1, -1, -1):
            return 1
        return 0

    while True:
        num_grids = read_int()
        if num_grids == 0:
            break
        result_list.append(process_grid(num_grids))

    return '\n'.join(str(element) for element in result_list)

print(main())