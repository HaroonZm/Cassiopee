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

sys.setrecursionlimit(10**7)
CONST_INF = 10**20
CONST_EPSILON = 1.0 / 10**10
CONST_MOD = 10**9 + 7
DIR_4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIR_8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def read_int_list(): return [int(x) for x in sys.stdin.readline().split()]
def read_int_list_decrement(): return [int(x)-1 for x in sys.stdin.readline().split()]
def read_float_list(): return [float(x) for x in sys.stdin.readline().split()]
def read_str_list(): return sys.stdin.readline().split()
def read_int(): return int(sys.stdin.readline())
def read_float(): return float(sys.stdin.readline())
def read_string(): return input()
def print_flush(s): return print(s, flush=True)

def main():
    result_list = []

    template_matrix = [
        [13, 7, 8, 0, 1, 2, 3],
        [7, 13, 0, 1, 9, 3, 4],
        [8, 0, 13, 2, 3, 10, 5],
        [0, 1, 2, 3, 4, 5, 6],
        [1, 9, 3, 4, 13, 6, 11],
        [2, 3, 10, 5, 6, 13, 12],
        [3, 4, 5, 6, 11, 12, 13]
    ]

    while True:
        input_str = read_string()
        if input_str == '#':
            break

        base_filter = [int(ch) for ch in input_str]
        pow2_list = [2**i for i in range(128)]
        state_map = {}
        for state_base3 in range(3**7):
            state_digits = []
            state_tmp = state_base3
            for _ in range(7):
                state_digits.append(state_tmp % 3)
                state_tmp //= 3
            if 2 in state_digits:
                continue
            state_digits.reverse()
            state_index = 0
            for val in state_digits:
                state_index *= 2
                state_index += val
            state_map[state_base3] = base_filter[state_index]

        for state_base3 in range(3**7):
            state_digits = []
            state_tmp = state_base3
            for _ in range(7):
                state_digits.append(state_tmp % 3)
                state_tmp //= 3
            if 2 not in state_digits:
                continue
            state_digits.reverse()
            first_two_idx = state_digits.index(2)
            e_val = 0
            y_val = 0
            for pos in range(7):
                e_val *= 3
                y_val *= 3
                if pos == first_two_idx:
                    y_val += 1
                else:
                    e_val += state_digits[pos]
                    y_val += state_digits[pos]

            val_e = state_map[e_val]
            val_y = state_map[y_val]
            if val_e == val_y:
                state_map[state_base3] = val_e
            else:
                state_map[state_base3] = 2

        is_valid = True
        for bit_pattern in range(2**13):
            bit_array = [1 if pow2_list[i] & bit_pattern else 0 for i in range(13)] + [2]
            calc_array = []
            for row_idx in range(7):
                tm_row = template_matrix[row_idx]
                enc = 0
                for cidx in tm_row:
                    enc *= 3
                    enc += bit_array[cidx]
                calc_array.append(state_map[enc])
            y_enc = 0
            for c in calc_array:
                y_enc *= 3
                y_enc += c
            if calc_array[3] != state_map[y_enc]:
                is_valid = False
                break

        if is_valid:
            result_list.append('yes')
        else:
            result_list.append('no')

    return '\n'.join(result_list)

print(main())