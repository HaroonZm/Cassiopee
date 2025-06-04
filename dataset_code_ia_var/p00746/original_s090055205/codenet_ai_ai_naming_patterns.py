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

# Constants
CONST_RECURSION_LIMIT = 10**7
CONST_INF = 10**20
CONST_EPS = 1.0 / 10**10
CONST_MOD = 10**9 + 7

sys.setrecursionlimit(CONST_RECURSION_LIMIT)

# Input functions
def input_int_list(): return [int(token) for token in sys.stdin.readline().split()]
def input_int_list_zero_based(): return [int(token) - 1 for token in sys.stdin.readline().split()]
def input_float_list(): return [float(token) for token in sys.stdin.readline().split()]
def input_str_list(): return sys.stdin.readline().split()
def input_single_int(): return int(sys.stdin.readline())
def input_single_float(): return float(sys.stdin.readline())
def input_single_str(): return input()
def print_flush(obj): return print(obj, flush=True)

def main():
    result_list = []

    direction_vectors = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    while True:
        value_n = input_single_int()
        if value_n == 0:
            break
        coords_list = [(0, 0)]
        for _ in range(value_n - 1):
            index_i, dir_idx = input_int_list()
            prev_coord = coords_list[index_i]
            delta = direction_vectors[dir_idx]
            coords_list.append((prev_coord[0] + delta[0], prev_coord[1] + delta[1]))
        y_list_sorted = sorted(coord[0] for coord in coords_list)
        x_list_sorted = sorted(coord[1] for coord in coords_list)
        width = x_list_sorted[-1] - x_list_sorted[0] + 1
        height = y_list_sorted[-1] - y_list_sorted[0] + 1
        result_list.append(f"{width} {height}")

    return '\n'.join(str(res) for res in result_list)

print(main())