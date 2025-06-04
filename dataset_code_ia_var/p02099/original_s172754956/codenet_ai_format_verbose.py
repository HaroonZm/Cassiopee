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

sys.setrecursionlimit(10 ** 7)

INFINITY_LARGE_NUMBER = 10 ** 20
MODULO_PRIME = 10 ** 9 + 7

def input_list_of_integers():
    return list(map(int, input().split()))

def input_list_of_floats():
    return list(map(float, input().split()))

def input_list_of_strings():
    return input().split()

def input_single_integer():
    return int(input())

def input_single_float():
    return float(input())

def input_single_string():
    return input()

def main():
    number_of_elements = input_single_integer()

    # list_of_pairs: each element is [value, original_index]
    list_of_value_index_pairs = sorted(
        [[input_single_float(), index] for index in range(number_of_elements)]
    )

    result_list = [0] * number_of_elements

    value_counts = collections.defaultdict(int)

    # Count occurrences of each unique value
    for value, original_index in list_of_value_index_pairs:
        value_counts[value] += 1

    current_max_value = -1
    current_max_index = 0

    for index_in_sorted_list in range(number_of_elements):
        value, original_index = list_of_value_index_pairs[index_in_sorted_list]

        if current_max_value < value:
            current_max_value = value
            current_max_index = index_in_sorted_list

        result_list[original_index] = current_max_index * 3 + value_counts[value] - 1

    return '\n'.join(map(str, result_list))

print(main())