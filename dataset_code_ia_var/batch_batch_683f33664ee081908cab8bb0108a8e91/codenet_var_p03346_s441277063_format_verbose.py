import bisect
import heapq
import math
import random
import sys

from collections import Counter, defaultdict
from decimal import Decimal, ROUND_CEILING, ROUND_HALF_UP
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product


def read_single_integer():
    return int(input())


def read_multiple_integers():
    return list(map(int, input().split()))


def read_single_float():
    return float(input())


def read_multiple_floats():
    return list(map(float, input().split()))


def read_single_string():
    return input()


def read_multiple_strings():
    return list(map(str, input().split()))


def measure_time(executed_function):
    import time

    def wrapper(*function_args, **function_kwargs):
        start_time = time.time()
        result = executed_function(*function_args, **function_kwargs)
        end_time = time.time()

        print(end_time - start_time, 'sec', file=sys.stderr)
        return result

    return wrapper


@measure_time
def solve_minimum_removals_for_sorted_subsequence(array_size, permutation_sequence):
    position_by_value = [-1] * array_size

    for original_index, value in enumerate(permutation_sequence):
        position_by_value[value - 1] = original_index

    previous_position = -1
    max_increasing_sequence_length = 0
    current_increasing_sequence_length = 0

    for current_position in position_by_value:
        if current_position > previous_position:
            current_increasing_sequence_length += 1
        else:
            current_increasing_sequence_length = 1

        max_increasing_sequence_length = max(max_increasing_sequence_length, current_increasing_sequence_length)
        previous_position = current_position

    minimum_removals = array_size - max_increasing_sequence_length
    return minimum_removals


def main():
    number_of_elements = read_single_integer()
    permutation_list = [read_single_integer() for _ in range(number_of_elements)]

    print(solve_minimum_removals_for_sorted_subsequence(number_of_elements, permutation_list))


if __name__ == '__main__':
    main()