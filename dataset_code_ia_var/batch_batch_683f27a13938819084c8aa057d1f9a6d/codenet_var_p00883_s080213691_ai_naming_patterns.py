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
DIR_4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIR_8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def read_ints(): return [int(x) for x in sys.stdin.readline().split()]
def read_ints_zero_based(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def read_floats(): return [float(x) for x in sys.stdin.readline().split()]
def read_strings(): return sys.stdin.readline().split()
def read_int(): return int(sys.stdin.readline())
def read_float(): return float(sys.stdin.readline())
def read_line(): return input()
def print_flush(s): return print(s, flush=True)

def main():
    result_list = []
    ok_states_dict = collections.defaultdict(set)

    def encode_grid_to_key(grid, size):
        key = 0
        for row in range(size):
            for col in range(size):
                key *= 3
                key += grid[row][col]
        return key

    def decode_key_to_grid(key, size):
        grid = []
        for row in range(size):
            current_row = []
            for col in range(size):
                current_row.append(key % 3)
                key //= 3
            grid.append(current_row[::-1])
        return grid

    def calc_next_states(current_grid, grid_size):
        pos_i = pos_j = -1
        for i in range(grid_size):
            for j in range(grid_size):
                if current_grid[i][j] == 2:
                    pos_i = i
                    pos_j = j
                    break
            if pos_i >= 0:
                break

        next_keys = set()
        current_grid[pos_i][pos_j] = 0
        for ni in range(max(0, pos_i - 1), min(grid_size, pos_i + 2)):
            for nj in range(max(0, pos_j - 1), min(grid_size, pos_j + 2)):
                if current_grid[ni][nj] != 0 or (pos_i == ni and pos_j == nj):
                    continue
                current_grid[ni][nj] = 2
                next_grid = [[0] * grid_size for _ in range(grid_size)]
                is_finished = True
                for r in range(grid_size):
                    for c in range(grid_size):
                        if current_grid[r][c] == 2:
                            continue
                        live_neighbors = 0
                        for nr in range(max(0, r - 1), min(grid_size, r + 2)):
                            for nc in range(max(0, c - 1), min(grid_size, c + 2)):
                                if nr == r and nc == c:
                                    continue
                                if current_grid[nr][nc] > 0:
                                    live_neighbors += 1
                        if (current_grid[r][c] == 0 and live_neighbors == 3) or (current_grid[r][c] == 1 and 2 <= live_neighbors <= 3):
                            next_grid[r][c] = 1
                            is_finished = False
                next_grid[ni][nj] = 2
                if is_finished:
                    return 'ok'
                next_keys.add(encode_grid_to_key(next_grid, grid_size))
                current_grid[ni][nj] = 0
        return next_keys

    def solve(grid_size):
        char_to_num = {'.': 0, '#': 1, '@': 2}
        grid = [[char_to_num[c] for c in read_line()] for _ in range(grid_size)]
        is_all_empty = True
        for i in range(grid_size):
            for j in range(grid_size):
                if grid[i][j] == 1:
                    is_all_empty = False
                    break
        if is_all_empty:
            return 0
        min_moves = CONST_INF
        state_dist = collections.defaultdict(lambda: CONST_INF)
        initial_key = encode_grid_to_key(grid, grid_size)
        pending_keys = set([initial_key])
        state_dist[initial_key] = 0
        moves_cnt = 0
        while pending_keys:
            moves_cnt += 1
            next_pending_keys = set()
            if pending_keys & ok_states_dict[grid_size]:
                return moves_cnt
            for key in pending_keys:
                cur_grid = decode_key_to_grid(key, grid_size)
                next_result = calc_next_states(cur_grid, grid_size)
                if next_result == 'ok':
                    ok_states_dict[grid_size].add(key)
                    return moves_cnt
                for next_key in next_result:
                    if state_dist[next_key] > moves_cnt:
                        state_dist[next_key] = moves_cnt
                        next_pending_keys.add(next_key)
            pending_keys = next_pending_keys
        return -1

    while True:
        field_size = read_int()
        if field_size == 0:
            break
        result_list.append(solve(field_size))

    return '\n'.join(map(str, result_list))

print(main())