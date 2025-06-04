#!/usr/bin/env python3

from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys
import random
import itertools
import math

sys.setrecursionlimit(10 ** 5)

standard_input = sys.stdin.readline
calculate_square_root = math.sqrt

def read_int_list():
    return list(map(int, standard_input().split()))

def read_float_list():
    return list(map(float, standard_input().split()))

def read_zero_based_int_list():
    return list(map(lambda x: int(x) - 1, standard_input().split()))

def read_single_int():
    return int(standard_input())

def read_single_float():
    return float(standard_input())

def read_list_of_strings():
    return list(map(list, standard_input().split()))

def read_stripped_string():
    return standard_input().rstrip()

def read_ints_n_lines(n):
    return [read_single_int() for _ in range(n)]

def read_int_lists_n_lines(n):
    return [read_int_list() for _ in range(n)]

def read_floats_n_lines(n):
    return [read_single_float() for _ in range(n)]

def read_float_lists_n_lines(n):
    return [read_float_list() for _ in range(n)]

def read_zero_based_int_lists_n_lines(n):
    return [read_zero_based_int_list() for _ in range(n)]

def read_strings_n_lines(n):
    return [read_stripped_string() for _ in range(n)]

def read_lists_of_strings_n_lines(n):
    return [read_list_of_strings() for _ in range(n)]

MODULO = 1000000007
INFINITY = 1e10
factorials = [1] * 1010
inverse_factorials = [1] * 1010
bernoulli_cache = [0] * 1010

def modulo_add(value1, value2=0):
    return (value1 + value2) % MODULO

def modulo_multiply(value1, value2=1):
    return (value1 * value2) % MODULO

def power_with_modulo(base, exponent):
    return pow(base, exponent, MODULO)

def modular_inverse(value):
    return power_with_modulo(value, MODULO - 2)

def bernoulli_number(index):
    if index > 0 and bernoulli_cache[index] == 0:
        bernoulli_cache[index] = modulo_add(1, modulo_multiply(index, bernoulli_number(index - 1)))
    return bernoulli_cache[index]

def solve():
    for index in range(1, 1010):
        factorials[index] = factorials[index - 1] * index
    for index in range(1010):
        inverse_factorials[index] = modular_inverse(factorials[index])

    current_num_blocks = 1
    dynamic_programming_table = [[[0] * 1010 for _ in range(2)] for _ in range(1010)]
    dp_cumulative = [0] * 1010
    block_type_is_f = [False] * 1010

    input_string_length = read_single_int()
    input_pattern_string = read_stripped_string()

    if input_string_length == 1 and input_pattern_string == "-":
        mid_value = (MODULO + 1) // 2
        print("{} 0 {}".format(mid_value, mid_value))
        return

    current_index = 0
    right_index = input_string_length
    block_index = -1

    if input_pattern_string[current_index] == "-":
        current_index += 1
    if input_pattern_string[current_index] == "-":
        current_index += 1
        block_index += 1
        current_num_blocks += 1
    if input_pattern_string[current_index] == "-":
        print("0 0 0")
        return

    for pattern_index in range(current_index, right_index):
        if input_pattern_string[pattern_index] == "X":
            if current_num_blocks == 0:
                print("0 0 0")
                return
            if block_index >= 0:
                block_type_is_f[block_index] = current_num_blocks - 1
            block_index += 1
            current_num_blocks = 0
        else:
            if current_num_blocks > 1:
                print("0 0 0")
                return
            current_num_blocks += 1

    if current_num_blocks == 2:
        block_type_is_f[block_index] = 1
        block_index += 1

    dp_cumulative[0] = 1
    num_blocks = block_index

    for i in range(num_blocks):
        if block_type_is_f[i]:
            for j in range(2):
                for k in range(2 * num_blocks + 2):
                    inverse_k_term = modular_inverse(k * k + 3 * k + 2)
                    dynamic_programming_table[i + 1][j][0] = modulo_add(
                        dynamic_programming_table[i + 1][j][0],
                        modulo_multiply(dynamic_programming_table[i][j][k], inverse_k_term)
                    )
                    dynamic_programming_table[i + 1][j][1] = modulo_add(
                        dynamic_programming_table[i + 1][j][1],
                        modulo_multiply(dynamic_programming_table[i][j][k], MODULO - inverse_k_term)
                    )
            dynamic_programming_table[i + 1][1][0] = modulo_add(
                dynamic_programming_table[i + 1][1][0],
                dp_cumulative[i]
            )
            dynamic_programming_table[i + 1][1][1] = modulo_add(
                dynamic_programming_table[i + 1][1][1],
                MODULO - dp_cumulative[i]
            )
        else:
            for j in range(2):
                for k in range(2 * num_blocks + 2):
                    inverse_k_plus_one = modular_inverse(k + 1)
                    dynamic_programming_table[i + 1][j][0] = modulo_add(
                        dynamic_programming_table[i + 1][j][0],
                        modulo_multiply(dynamic_programming_table[i][j][k], inverse_k_plus_one)
                    )
                    dynamic_programming_table[i + 1][j][1] = modulo_add(
                        dynamic_programming_table[i + 1][j][1],
                        modulo_multiply(dynamic_programming_table[i][j][k], MODULO - inverse_k_plus_one)
                    )
                    dynamic_programming_table[i + 1][j][k + 2] = modulo_add(
                        dynamic_programming_table[i + 1][j][k + 2],
                        modulo_multiply(dynamic_programming_table[i][j][k], modular_inverse(k * k + 3 * k + 2))
                    )
            dynamic_programming_table[i + 1][1][1] = modulo_add(
                dynamic_programming_table[i + 1][1][1],
                dp_cumulative[i]
            )
            dynamic_programming_table[i + 1][1][0] = modulo_add(
                dynamic_programming_table[i + 1][1][0],
                MODULO - dp_cumulative[i]
            )
            dp_cumulative[i + 1] = modulo_add(dp_cumulative[i + 1], dp_cumulative[i])

    result_counts = [0] * 3

    for j in range(2):
        for k in range(2 * num_blocks + 2):
            result_counts[j] = modulo_add(
                result_counts[j],
                modulo_multiply(dynamic_programming_table[num_blocks][j][k], factorials[k])
            )
            result_counts[j + 1] = modulo_add(
                result_counts[j + 1],
                modulo_multiply(dynamic_programming_table[num_blocks][j][k], MODULO - modulo_add(factorials[k], bernoulli_number(k)))
            )

    mid_value = (MODULO + 1) // 2
    result_counts[0] = modulo_add(result_counts[0], modulo_multiply(dp_cumulative[num_blocks], mid_value))
    result_counts[2] = modulo_add(result_counts[2], modulo_multiply(dp_cumulative[num_blocks], MODULO - mid_value))

    print("{} {} {}".format(result_counts[0], result_counts[1], result_counts[2]))
    return

if __name__ == '__main__':
    solve()