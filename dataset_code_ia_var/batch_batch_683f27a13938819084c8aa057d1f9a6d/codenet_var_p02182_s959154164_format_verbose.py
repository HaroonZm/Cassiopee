import sys

from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
import random

def read_int_list_from_input():
    return [int(value) for value in sys.stdin.readline().split()]

def read_single_int_from_input():
    return int(sys.stdin.readline())

def read_list_of_char_lists_from_input():
    return [list(token) for token in sys.stdin.readline().split()]

def read_char_list_from_input():
    line_as_list = list(sys.stdin.readline())
    if line_as_list and line_as_list[-1] == "\n":
        return line_as_list[:-1]
    return line_as_list

def read_multiple_single_ints(number_of_inputs):
    return [read_single_int_from_input() for _ in range(number_of_inputs)]

def read_multiple_int_lists(number_of_inputs):
    return [read_int_list_from_input() for _ in range(number_of_inputs)]

def read_multiple_char_lists(number_of_inputs):
    return [read_char_list_from_input() for _ in range(number_of_inputs)]

def read_multiple_list_of_char_lists(number_of_inputs):
    return [read_list_of_char_lists_from_input() for _ in range(number_of_inputs)]

sys.setrecursionlimit(1000000)

MODULO_CONSTANT = 1000000007

def count_cell_differences_between_matrices():
    number_of_rows, number_of_columns = read_int_list_from_input()

    matrix_a = read_multiple_char_lists(number_of_rows)
    matrix_b = read_multiple_char_lists(number_of_rows)

    total_cell_difference_count = 0

    for row_index in range(number_of_rows):
        for column_index in range(number_of_columns):
            if matrix_a[row_index][column_index] != matrix_b[row_index][column_index]:
                total_cell_difference_count += 1

    print(total_cell_difference_count)
    return

if __name__ == "__main__":
    count_cell_differences_between_matrices()