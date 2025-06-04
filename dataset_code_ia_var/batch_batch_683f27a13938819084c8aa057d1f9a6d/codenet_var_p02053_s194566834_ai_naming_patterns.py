import sys
from operator import itemgetter
from fractions import gcd
from math import ceil, floor
from copy import deepcopy
from itertools import accumulate
from collections import Counter
import math
from functools import reduce

sys.setrecursionlimit(200000)

# Input function definitions
def input_line(): return sys.stdin.readline()
def input_int(): return int(input_line())
def input_ints(): return map(int, input_line().rstrip().split())
def input_int_list(): return list(map(int, input_line().rstrip().split()))
def input_str_list(): return list(input_line().rstrip())

def debug_log(*dbg_args, dbg_sep=" ", dbg_end="\n"):
    if not __debug__:
        print("debug:", *dbg_args, file=sys.stderr, sep=dbg_sep, end=dbg_end)

height_val, width_val = input_ints()
grid_data = [input_str_list() for idx_row in range(height_val)]
black_pos_list = []
for row_idx in range(height_val):
    for col_idx in range(width_val):
        if grid_data[row_idx][col_idx] == "B":
            black_pos_list.append((row_idx, col_idx))

black_pos_list.sort(key=lambda pos: pos[0] + pos[1])
debug_log(black_pos_list[-1])
debug_log(black_pos_list[0])
max_dist_diag1 = abs(black_pos_list[-1][0] - black_pos_list[0][0]) + abs(black_pos_list[-1][1] - black_pos_list[0][1])

black_pos_list.sort(key=lambda pos: pos[0] + (width_val - pos[1]))
debug_log(black_pos_list[-1])
debug_log(black_pos_list[0])
max_dist_diag2 = abs(black_pos_list[-1][0] - black_pos_list[0][0]) + abs(black_pos_list[-1][1] - black_pos_list[0][1])

print(max(max_dist_diag1, max_dist_diag2))