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

# Constantes système et conventions de nommage
SYSTEM_RECURSION_LIMIT = 10 ** 7
VALUE_INFINITY = 10 ** 20
EPSILON = 1.0 / 10 ** 10
MODULUS = 10 ** 9 + 7
DIRECTION_4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRECTION_8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

sys.setrecursionlimit(SYSTEM_RECURSION_LIMIT)

def input_list_int(): return [int(value) for value in sys.stdin.readline().split()]
def input_list_int_offset(): return [int(value) - 1 for value in sys.stdin.readline().split()]
def input_list_float(): return [float(value) for value in sys.stdin.readline().split()]
def input_list_str(): return sys.stdin.readline().split()
def input_single_int(): return int(sys.stdin.readline())
def input_single_float(): return float(sys.stdin.readline())
def input_single_str(): return input()
def print_flush(output): return print(output, flush=True)

class PrefixSum2D:
    def __init__(self, grid_2d):
        self.num_rows = num_rows = len(grid_2d)
        self.num_cols = num_cols = len(grid_2d[0])
        self.prefix_sum = psum = [row[:] for row in grid_2d]

        for row_idx in range(num_rows):
            for col_idx in range(1, num_cols):
                psum[row_idx][col_idx] += psum[row_idx][col_idx - 1]
        for row_idx in range(1, num_rows):
            for col_idx in range(num_cols):
                psum[row_idx][col_idx] += psum[row_idx - 1][col_idx]

    def range_sum(self, top, left, bottom, right):
        if top > bottom or left > right:
            return 0
        psum = self.prefix_sum
        total = psum[bottom][right]
        if top > 0 and left > 0:
            return total - psum[top - 1][right] - psum[bottom][left - 1] + psum[top - 1][left - 1]
        if left > 0:
            total -= psum[bottom][left - 1]
        if top > 0:
            total -= psum[top - 1][right]
        return total

def main_process():
    num_points, num_queries = input_list_int()
    points = [input_list_int() for _ in range(num_points)]
    unique_x = set()
    unique_y = set()
    for x_value, y_value in points:
        unique_x.add(x_value)
        unique_y.add(y_value)

    sorted_x_list = sorted(unique_x)
    sorted_y_list = sorted(unique_y)
    x_index_map = {value: idx for idx, value in enumerate(sorted_x_list)}
    y_index_map = {value: idx for idx, value in enumerate(sorted_y_list)}

    grid_count = [[0] * (len(sorted_y_list) + 1) for _ in range(len(sorted_x_list) + 1)]
    for x_value, y_value in points:
        grid_count[x_index_map[x_value]][y_index_map[y_value]] += 1

    prefix_sum_2d = PrefixSum2D(grid_count)
    result_output = []
    for _ in range(num_queries):
        query_x1, query_y1, query_x2, query_y2 = input_list_int()
        x_query_left = bisect.bisect_left(sorted_x_list, query_x1)
        y_query_top = bisect.bisect_left(sorted_y_list, query_y1)
        x_query_right = bisect.bisect(sorted_x_list, query_x2) - 1
        y_query_bottom = bisect.bisect(sorted_y_list, query_y2) - 1
        result_output.append(prefix_sum_2d.range_sum(y_query_top, x_query_left, y_query_bottom, x_query_right))
    return '\n'.join(map(str, result_output))

print(main_process())