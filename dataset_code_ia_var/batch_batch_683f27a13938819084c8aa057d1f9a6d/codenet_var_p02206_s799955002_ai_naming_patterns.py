import sys
from itertools import *
from bisect import *
from math import *
from collections import *
from heapq import *
from random import *

sys.setrecursionlimit(10 ** 6)

def to_zero_indexed_int(x): return int(x) - 1
def print_2d_list(lst): print(*lst, sep="\n")

def input_int(): return int(sys.stdin.readline())
def input_ints(): return map(int, sys.stdin.readline().split())
def input_zero_indexed_ints(): return map(to_zero_indexed_int, sys.stdin.readline().split())
def input_floats(): return map(float, sys.stdin.readline().split())
def input_int_list(): return list(map(int, sys.stdin.readline().split()))
def input_zero_indexed_int_list(): return list(map(to_zero_indexed_int, sys.stdin.readline().split()))
def input_float_list(): return list(map(float, sys.stdin.readline().split()))
def input_multi_int_lists(row_count): return [input_int_list() for _ in range(row_count)]

FOUR_DIRECTION_DELTAS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def main():
    def is_valid(mid_value):
        current_sum = 0
        count = 0
        value = mid_value
        while value:
            current_sum += value
            count += 1
            if current_sum > max_sum: return False
            if count == total_count: break
            value >>= 1
        return True

    total_count, max_sum = input_ints()
    left = 0
    right = max_sum + 1
    while left + 1 < right:
        mid = (left + right) // 2
        if is_valid(mid):
            left = mid
        else:
            right = mid
    print(left)

main()