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
CONST_EPS = 1.0 / 10**10
CONST_MOD = 10**9 + 7
MOVE_DIRS_4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
MOVE_DIRS_8 = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

def read_int_list(): return [int(x) for x in sys.stdin.readline().split()]
def read_int_list_0idx(): return [int(x)-1 for x in sys.stdin.readline().split()]
def read_float_list(): return [float(x) for x in sys.stdin.readline().split()]
def read_str_list(): return sys.stdin.readline().split()
def read_int(): return int(sys.stdin.readline())
def read_float(): return float(sys.stdin.readline())
def read_str(): return input()
def print_flush(val): return print(val, flush=True)

def main():
    row_count, col_count = read_int_list()
    grid = ['#' * (col_count + 2)]
    for _ in range(row_count):
        grid.append('#' + read_str() + '#')
    grid.append('#' * (col_count + 2))
    state = (-1, -1, -1)
    for r_idx in range(1, row_count + 1):
        for c_idx in range(col_count + 1):
            cell_value = grid[r_idx][c_idx]
            if cell_value == '^':
                state = (r_idx, c_idx, 0, 1)
            elif cell_value == '>':
                state = (r_idx, c_idx, 1, 1)
            elif cell_value == 'v':
                state = (r_idx, c_idx, 2, 1)
            elif cell_value == '<':
                state = (r_idx, c_idx, 3, 1)
    visited_state_dict = collections.defaultdict(bool)
    visited_position_set = set()
    result_counter = -1
    turn_transitions = [
        [(-1,1), (0,1), (1,1)],
        [(1,1), (1,0), (1,-1)],
        [(1,-1), (0,-1), (-1,-1)],
        [(-1,-1), (-1,0), (-1,1)]
    ]
    while True:
        if visited_state_dict[state]:
            return -1
        visited_state_dict[state] = True
        curr_r, curr_c, curr_dir, curr_k = state
        visited_position_set.add((curr_r, curr_c))
        if grid[curr_r][curr_c] == 'G':
            return len(visited_position_set)
        if curr_k < 2:
            next_r = curr_r + MOVE_DIRS_4[curr_dir][0]
            next_c = curr_c + MOVE_DIRS_4[curr_dir][1]
            if grid[next_r][next_c] != '#':
                result_counter += 1
                state = (next_r, next_c, curr_dir, curr_k + 1)
            else:
                state = (curr_r, curr_c, (curr_dir - 1) % 4, 1)
        else:
            next_dir = (curr_dir + 1) % 4
            next_diag_r = curr_r + MOVE_DIRS_4[next_dir][0]
            next_diag_c = curr_c + MOVE_DIRS_4[next_dir][1]
            if grid[next_diag_r][next_diag_c] == '#':
                state = (curr_r, curr_c, curr_dir, 1)
            else:
                state = (curr_r, curr_c, next_dir, 0)
    return -1

print(main())