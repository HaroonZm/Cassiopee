import sys
import math
import itertools as it
from collections import deque

sys.setrecursionlimit(1000000)

CONST_INF = 10 ** 18
CONST_MOD = 10 ** 9 + 7

def process_query(depth_size, coord_y, coord_x):
    y_sequence = [coord_y]
    cur_y = coord_y
    for idx_level in range(1, depth_size)[::-1]:
        level_width = 2 ** idx_level
        if cur_y <= level_width:
            cur_y = level_width - cur_y + 1
        else:
            cur_y -= level_width
        y_sequence = [cur_y] + y_sequence
    label_sequence = ""
    cur_y = 1
    for idx_depth in range(depth_size):
        seg_size = 2 ** (depth_size - idx_depth)
        is_right = (coord_x > seg_size // 2) ^ (cur_y + 2 ** idx_depth == y_sequence[idx_depth])
        next_label = "R" if is_right else "L"
        if next_label == "L":
            if coord_x <= seg_size // 2:
                coord_x = seg_size // 2 - coord_x + 1
            else:
                coord_x -= seg_size // 2
        else:
            if coord_x > seg_size // 2:
                coord_x = seg_size - coord_x + 1
        label_sequence += next_label
        cur_y = y_sequence[idx_depth]
    return label_sequence

while True:
    input_line = raw_input()
    if not input_line:
        continue
    input_n, input_y, input_x = map(int, input_line.strip().split())
    if input_n == 0:
        break
    result_labels = process_query(input_n, input_y, input_x)
    print result_labels