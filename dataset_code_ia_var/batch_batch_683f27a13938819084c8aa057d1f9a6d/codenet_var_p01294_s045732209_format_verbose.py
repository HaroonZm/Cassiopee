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

sys.setrecursionlimit(10 ** 7)

INFINITY = 10 ** 20
EPSILON = 1.0 / (10 ** 10)
MODULUS = 10 ** 9 + 7

FOUR_DIRECTION_DELTAS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
EIGHT_DIRECTION_DELTAS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def read_int_list():
    return [int(x) for x in sys.stdin.readline().split()]

def read_int_list_zero_indexed():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def read_float_list():
    return [float(x) for x in sys.stdin.readline().split()]

def read_string_list():
    return sys.stdin.readline().split()

def read_single_int():
    return int(sys.stdin.readline())

def read_single_float():
    return float(sys.stdin.readline())

def read_input_string():
    return input()

def print_flush(output_string):
    print(output_string, flush=True)

def main():
    result_output_lines = []

    while True:
        num_groups, difference_threshold = read_int_list()
        
        if num_groups == 0:
            break

        all_group_members = []
        for _ in range(num_groups):
            group_information = read_int_list()
            member_values = group_information[1:]
            all_group_members.append(member_values)

        group_sum_and_members_list = []
        for members in all_group_members:
            group_sum = sum(members)
            group_sum_and_members_list.append([group_sum, members])

        is_processing = True

        while is_processing:
            is_processing = False

            group_sum_and_members_list.sort()
            current_max_group_sum, current_max_group_members = group_sum_and_members_list[-1]

            if current_max_group_sum == 0:
                break

            second_largest_group_sum = group_sum_and_members_list[-2][0]

            if current_max_group_sum - current_max_group_members[-1] >= second_largest_group_sum - difference_threshold:
                group_sum_and_members_list[-1] = [current_max_group_sum - current_max_group_members[-1], current_max_group_members[:-1]]
                is_processing = True
                continue

            for group_index in range(num_groups-2, -1, -1):
                group_sum, group_members = group_sum_and_members_list[group_index]

                if group_sum == 0:
                    break

                if group_sum - group_members[-1] >= current_max_group_sum - difference_threshold:
                    group_sum_and_members_list[group_index] = [group_sum - group_members[-1], group_members[:-1]]
                    is_processing = True

        if group_sum_and_members_list[-1][0] == 0:
            result_output_lines.append('Yes')
        else:
            result_output_lines.append('No')

    return '\n'.join(map(str, result_output_lines))

print(main())