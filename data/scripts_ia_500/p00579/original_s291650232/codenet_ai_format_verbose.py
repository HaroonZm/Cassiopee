import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

from math import floor, ceil, sqrt, factorial, log
from heapq import heappop, heappush, heappushpop
from collections import Counter, defaultdict, deque
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right
from copy import deepcopy

INFINITY = float('inf')
MODULUS = 10**9 + 7


def print_matrix_separately(*matrices):
    for matrix in matrices:
        print(*matrix, sep='\n')


def convert_to_zero_indexed(integer_string):
    return int(integer_string) - 1


def map_to_integers():
    return map(int, input().split())


def map_to_floats():
    return map(float, input().split())


def map_to_zero_indexed_integers():
    return map(convert_to_zero_indexed, input().split())


def list_of_integers():
    return list(map_to_integers())


def list_of_zero_indexed_integers():
    return [int(element) - 1 for element in input().split()]


def list_of_floats():
    return list(map_to_floats())


def list_of_lines_as_integers(number_of_lines: int):
    return [read_single_integer() for _ in range(number_of_lines)]


def list_of_integer_lists(number_of_lines: int):
    return [list_of_integers() for _ in range(number_of_lines)]


def list_of_zero_indexed_integer_lists(number_of_lines: int):
    return [list_of_zero_indexed_integers() for _ in range(number_of_lines)]


def list_of_lines_strings_to_integer_lists():
    return [list(map(int, line.split())) for line in input()]


def read_single_integer():
    return int(input())


def read_single_float():
    return float(input())


def read_and_strip_string():
    return input().replace('\n', '')


def main():
    number_of_trees, number_of_forbidden_intervals = map_to_integers()

    brightness_values = list_of_integers()

    forbidden_intervals_zero_indexed = []

    for _ in range(number_of_forbidden_intervals):
        left_index_zero_based, right_index_zero_based = map_to_zero_indexed_integers()
        forbidden_intervals_zero_indexed.append((left_index_zero_based, right_index_zero_based))

    forbidden_intervals_zero_indexed.sort()

    # At each tree index, store the leftmost forbidden interval start index covering this tree
    leftmost_forbidden_interval_start_for_tree = [index for index in range(number_of_trees)]

    current_processing_index = 0

    for interval_start, interval_end in forbidden_intervals_zero_indexed:
        for tree_index in range(max(current_processing_index, interval_start), interval_end + 1):
            leftmost_forbidden_interval_start_for_tree[tree_index] = interval_start
            current_processing_index = tree_index + 1

    # dp[i]: maximum achievable brightness from trees 0 to i without using overlapping forbidden intervals
    max_brightness_up_to_index = [0] * number_of_trees

    max_brightness_up_to_index[0] = brightness_values[0]

    for tree_index in range(1, number_of_trees):
        if leftmost_forbidden_interval_start_for_tree[tree_index] == 0:
            max_brightness_up_to_index[tree_index] = max(
                max_brightness_up_to_index[tree_index - 1], brightness_values[tree_index]
            )
        else:
            max_brightness_up_to_index[tree_index] = max(
                max_brightness_up_to_index[tree_index - 1],
                brightness_values[tree_index] + max_brightness_up_to_index[leftmost_forbidden_interval_start_for_tree[tree_index] - 1],
            )

    print(max_brightness_up_to_index[-1])


if __name__ == "__main__":
    main()