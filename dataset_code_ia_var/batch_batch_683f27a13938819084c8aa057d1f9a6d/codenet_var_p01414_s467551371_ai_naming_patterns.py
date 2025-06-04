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
CONST_EPS = 1.0 / 10**13
CONST_MOD = 10**9 + 7
DIRS_4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRS_8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def input_int_list(): return [int(val) for val in sys.stdin.readline().split()]
def input_int_list_zero(): return [int(val) - 1 for val in sys.stdin.readline().split()]
def input_float_list(): return [float(val) for val in sys.stdin.readline().split()]
def input_str_list(): return sys.stdin.readline().split()
def input_int(): return int(sys.stdin.readline())
def input_float(): return float(sys.stdin.readline())
def input_str(): return input()
def print_flush(obj): print(obj, flush=True)

def main():
    result_list = []

    def solve_case(num_rects):
        rect_list = [input_int_list() for _ in range(num_rects)]
        color_board = []
        for _ in range(4):
            color_board += [ch for ch in input_str()]
        masks_set = set()
        full_mask = (1 << 16) - 1
        bit_indices = [1 << idx for idx in range(16)]
        for rect_height, rect_width in rect_list:
            for top in range(-rect_height + 1, 4):
                for left in range(-rect_width + 1, 4):
                    mask = full_mask
                    for row in range(max(0, top), min(4, top + rect_height)):
                        for col in range(max(0, left), min(4, left + rect_width)):
                            mask -= bit_indices[row * 4 + col]
                    masks_set.add(mask)
        color_mask_pairs = []
        for partial_mask in masks_set:
            for color in 'RGB':
                color_val_mask = 0
                for idx in range(16):
                    if bit_indices[idx] & partial_mask:
                        continue
                    if color_board[idx] == color:
                        color_val_mask += bit_indices[idx]
                if color_val_mask > 0:
                    color_mask_pairs.append((partial_mask, color_val_mask))

        visited_dict = collections.defaultdict(bool)
        state_set = set([0])
        move_count = 0
        while state_set:
            move_count += 1
            next_state_set = set()
            for state in state_set:
                visited_dict[state] = True
            for state in state_set:
                for pmask, cval_mask in color_mask_pairs:
                    new_state = (state & pmask) + cval_mask
                    if visited_dict[new_state]:
                        continue
                    if new_state == full_mask:
                        return move_count
                    next_state_set.add(new_state)
            state_set = next_state_set

        return -1

    while True:
        num_cases = input_int()
        if num_cases == 0:
            break
        result_list.append(solve_case(num_cases))
        break

    return '\n'.join(map(str, result_list))

print(main())