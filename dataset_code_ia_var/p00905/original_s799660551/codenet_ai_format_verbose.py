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

# Augmentation de la limite de récursion 
sys.setrecursionlimit(10**7)

INFINITE_NUMBER = 10**20
EPSILON = 1.0 / 10**10
MODULO = 10**9 + 7

CARDINAL_DIRECTIONS = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]
DIAGONAL_AND_CARDINAL_DIRECTIONS = [
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, -1),
    (-1, 0),
    (-1, 1)
]

def read_int_list():
    return [int(x) for x in sys.stdin.readline().split()]

def read_int_list_zero_based():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def read_float_list():
    return [float(x) for x in sys.stdin.readline().split()]

def read_string_list():
    return sys.stdin.readline().split()

def read_single_int():
    return int(sys.stdin.readline())

def read_single_float():
    return float(sys.stdin.readline())

def read_single_line_string():
    return input()

def print_flush(output_value):
    print(output_value, flush=True)

def main():
    output_results_per_case = []

    while True:
        num_reference_lines, num_query_lines = read_int_list()
        
        if num_reference_lines == 0:
            break

        reference_lines = [read_single_line_string() for _ in range(num_reference_lines)]
        query_lines = [read_single_line_string() for _ in range(num_query_lines)]

        # Store incremental info about open/close counts and leading dots per reference line
        reference_bracket_state_per_line = [[0, 0, 0, 0]]  # (round, curly, square, leadDots)
        max_leading_dots = 0

        for reference_line in reference_lines:
            character_counter = collections.Counter(reference_line)
            latest_state = reference_bracket_state_per_line[-1][:]

            latest_state[0] += character_counter['(']
            latest_state[0] -= character_counter[')']
            latest_state[1] += character_counter['{']
            latest_state[1] -= character_counter['}']
            latest_state[2] += character_counter['[']
            latest_state[2] -= character_counter[']']
            latest_state[3] = 0

            for char in reference_line:
                if char != '.':
                    break
                latest_state[3] += 1
                if max_leading_dots < latest_state[3]:
                    max_leading_dots = latest_state[3]

            reference_bracket_state_per_line.append(latest_state[:])

        valid_coefficients = []
        max_possible_leading_dots = min(max_leading_dots + 1, 21)

        # Test all possible combinations of coefficients (c1,c2,c3) in range 1..max_leading_dots or 20
        for round_bracket_coeff, curly_bracket_coeff, square_bracket_coeff in itertools.product(
                range(1, max_possible_leading_dots), repeat=3):

            is_valid_coefficients = True

            for line_idx in range(num_reference_lines):
                bracket_state = reference_bracket_state_per_line[line_idx]

                computed_leading_dots = (
                    bracket_state[0] * round_bracket_coeff +
                    bracket_state[1] * curly_bracket_coeff +
                    bracket_state[2] * square_bracket_coeff
                )

                expected_leading_dots = reference_bracket_state_per_line[line_idx + 1][3]

                if computed_leading_dots != expected_leading_dots:
                    is_valid_coefficients = False
                    break

            if is_valid_coefficients:
                valid_coefficients.append(
                    (round_bracket_coeff, curly_bracket_coeff, square_bracket_coeff)
                )

        query_bracket_state_per_line = [[0, 0, 0]]

        for query_line in query_lines:
            query_counter = collections.Counter(query_line)
            latest_query_state = query_bracket_state_per_line[-1][:]

            latest_query_state[0] += query_counter['(']
            latest_query_state[0] -= query_counter[')']
            latest_query_state[1] += query_counter['{']
            latest_query_state[1] -= query_counter['}']
            latest_query_state[2] += query_counter['[']
            latest_query_state[2] -= query_counter[']']

            query_bracket_state_per_line.append(latest_query_state[:])

        indentations_for_queries = [0]

        # For each query line (excluding the first and last, since the first is always 0 by convention)
        for bracket_state in query_bracket_state_per_line[1:-1]:
            possible_indentation_values = set()

            for round_bracket_coeff, curly_bracket_coeff, square_bracket_coeff in valid_coefficients:
                indentation = (
                    bracket_state[0] * round_bracket_coeff +
                    bracket_state[1] * curly_bracket_coeff +
                    bracket_state[2] * square_bracket_coeff
                )
                possible_indentation_values.add(indentation)

            if len(possible_indentation_values) == 1:
                indentations_for_queries.append(list(possible_indentation_values)[0])
            elif sum(bracket_state) == 0:
                # If all bracket counts are balanced, indentation should be zero.
                indentations_for_queries.append(0)
            else:
                indentations_for_queries.append(-1)

        output_results_per_case.append(' '.join(map(str, indentations_for_queries)))

    return '\n'.join(map(str, output_results_per_case))

print(main())