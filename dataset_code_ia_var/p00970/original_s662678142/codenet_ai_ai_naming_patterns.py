import array
from fractions import Fraction
import functools
import itertools
import math
import os
import sys

def main_entry():
    row_count, col_count, point_count = read_int_list()
    point_list = []
    for _ in range(point_count):
        row_idx, col_idx = read_int_list()
        row_idx -= 1
        col_idx -= 1
        point_list.append((row_idx, col_idx))

    print(compute_result(row_count, col_count, point_count, point_list))

def compute_result(row_count, col_count, point_count, point_list):
    placement_counts = [0] * (row_count + col_count + 1)
    for row_idx, col_idx in point_list:
        diagonal_offset = col_count - col_idx if col_idx < col_count else col_idx - col_count + 1
        placement_counts[row_count - 1 - row_idx + diagonal_offset] += 1

    overflow_count = 0
    for idx in range(row_count + col_count + 1):
        total = placement_counts[idx] + overflow_count
        if total > 0:
            placement_counts[idx] = 1
            overflow_count = total - 1
    if overflow_count > 0:
        return row_count + col_count + 1 + overflow_count
    while placement_counts and placement_counts[-1] == 0:
        placement_counts.pop()
    return len(placement_counts)

DEBUG_MODE = 'DEBUG' in os.environ

def read_line():
    return sys.stdin.readline().rstrip()

def read_int_value():
    return int(read_line())

def read_int_list():
    return [int(element) for element in read_line().split()]

def debug_print(*content, sep=' ', end='\n'):
    if DEBUG_MODE:
        print(*content, sep=sep, end=end)

if __name__ == '__main__':
    main_entry()