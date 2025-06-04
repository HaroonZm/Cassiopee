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
CONST_INF = 10 ** 20
CONST_EPS = 1.0 / 10 ** 10
CONST_MOD = 998244353
DIR_4 = [(0, -1), (1, 0), (0, 1), (-1, 0)]
DIR_8 = [
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
]

def read_int_list(): return [int(token) for token in sys.stdin.readline().split()]
def read_int_list_zero_based(): return [int(token) - 1 for token in sys.stdin.readline().split()]
def read_float_list(): return [float(token) for token in sys.stdin.readline().split()]
def read_str_list(): return sys.stdin.readline().split()
def read_int(): return int(sys.stdin.readline())
def read_float(): return float(sys.stdin.readline())
def read_str(): return input()
def print_flush(output): return print(output, flush=True)

def process_main():
    result_list = []

    while True:
        input_n, input_m = read_int_list()
        arr_b = read_int_list()
        arr_p = read_int_list()
        min_result = CONST_INF

        temp_pattern = []
        for pattern_idx in range(input_m):
            temp_pattern += [pattern_idx % 2] * arr_p[pattern_idx]
        if sorted(collections.Counter(temp_pattern).items()) == sorted(collections.Counter(arr_b).items()):
            temp_total = 0
            b_pos = 0
            for idx in range(input_n):
                if temp_pattern[idx] != 1:
                    continue
                while arr_b[b_pos] != 1:
                    b_pos += 1
                temp_total += abs(idx - b_pos)
                b_pos += 1
            min_result = temp_total

        temp_pattern = []
        for pattern_idx in range(input_m):
            temp_pattern += [(pattern_idx + 1) % 2] * arr_p[pattern_idx]
        if sorted(collections.Counter(temp_pattern).items()) == sorted(collections.Counter(arr_b).items()):
            temp_total = 0
            b_pos = 0
            for idx in range(input_n):
                if temp_pattern[idx] != 1:
                    continue
                while arr_b[b_pos] != 1:
                    b_pos += 1
                temp_total += abs(idx - b_pos)
                b_pos += 1
            if min_result > temp_total:
                min_result = temp_total
        result_list.append(min_result)
        break

    return '\n'.join(map(str, result_list))

print(process_main())