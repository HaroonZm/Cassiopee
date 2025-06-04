import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np

read_str_line = lambda: sys.stdin.readline().rstrip()
read_str_tokens = lambda: map(str, sys.stdin.buffer.readline().split())
read_int = lambda: int(sys.stdin.readline())
read_int_tokens = lambda: map(int, sys.stdin.buffer.readline().split())
read_int_list = lambda: list(map(int, sys.stdin.buffer.readline().split()))

input_str = read_str_line()
repeat_count = read_int()
pair_count_single = 0
index_single = 0

if len(set(input_str)) == 1:
    print(int(len(input_str) * repeat_count // 2))
    sys.exit()

while index_single < len(input_str) - 1:
    if input_str[index_single] == input_str[index_single + 1]:
        pair_count_single += 1
        index_single += 1
    index_single += 1

pair_count_double = 0
index_double = 0
double_str = input_str * 2

while index_double < len(double_str) - 1:
    if double_str[index_double] == double_str[index_double + 1]:
        pair_count_double += 1
        index_double += 1
    index_double += 1

result = (pair_count_double - pair_count_single) * (repeat_count - 1) + pair_count_single
print(result)