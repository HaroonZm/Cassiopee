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

INFINITE_INT = 10 ** 20
FLOAT_EPSILON = 1.0 / (10 ** 13)
MODULO_VALUE = 10 ** 9 + 7
FOUR_DIRECTION_VECTORS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
EIGHT_DIRECTION_VECTORS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def get_list_of_ints():
    return [int(x) for x in sys.stdin.readline().split()]

def get_list_of_ints_zero_based():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def get_list_of_floats():
    return [float(x) for x in sys.stdin.readline().split()]

def get_list_of_strings():
    return sys.stdin.readline().split()

def get_single_int():
    return int(sys.stdin.readline())

def get_single_float():
    return float(sys.stdin.readline())

def get_single_string():
    return input()

def print_flush(output_value):
    print(output_value, flush=True)

def main():
    computed_results = []

    def compute_maximum_value_by_inserting_operators(dot_separated_binary_string):
        allowed_characters = '01+-*()'
        binary_number_blocks = dot_separated_binary_string.split('.')
        maximum_result = -1
        num_blocks = len(binary_number_blocks)
        memoized_expressions = {}

        def evaluate_expression(expression_string):
            if expression_string in memoized_expressions:
                return memoized_expressions[expression_string]

            if ')' in expression_string:
                closing_parenthesis_index = expression_string.index(')')
                # Ensure no digit immediately after closing parenthesis
                if len(expression_string) > closing_parenthesis_index + 1 and expression_string[closing_parenthesis_index + 1] in '01':
                    memoized_expressions[expression_string] = -1
                    return -1
                opening_parenthesis_index = -1
                for idx in range(closing_parenthesis_index - 1, -1, -1):
                    if expression_string[idx] == '(':
                        opening_parenthesis_index = idx
                        break
                # No matching opening parenthesis or left parenthesis precedes a digit
                if opening_parenthesis_index < 0 or (opening_parenthesis_index > 0 and expression_string[opening_parenthesis_index - 1] in '01'):
                    memoized_expressions[expression_string] = -1
                    return -1
                sub_expression = expression_string[opening_parenthesis_index + 1:closing_parenthesis_index]
                if '+' not in sub_expression and '-' not in sub_expression and '*' not in sub_expression:
                    memoized_expressions[expression_string] = -1
                    return -1
                evaluated_sub = evaluate_expression(sub_expression)
                if evaluated_sub == -1:
                    memoized_expressions[expression_string] = -1
                    return -1
                new_expression = expression_string[:opening_parenthesis_index] + evaluated_sub + expression_string[closing_parenthesis_index + 1:]
                memoized_expressions[expression_string] = evaluate_expression(new_expression)
                return memoized_expressions[expression_string]

            if '(' in expression_string:
                memoized_expressions[expression_string] = -1
                return -1

            expression_length = len(expression_string)
            # Multiplication handling
            if '*' in expression_string:
                multiply_index = expression_string.index('*')
                left_num_start = multiply_index
                for idx in range(multiply_index - 1, -1, -1):
                    if expression_string[idx] not in '01':
                        break
                    left_num_start = idx
                right_num_end = multiply_index
                for idx in range(multiply_index + 1, expression_length):
                    if expression_string[idx] not in '01':
                        break
                    right_num_end = idx
                if left_num_start == multiply_index or right_num_end == multiply_index:
                    memoized_expressions[expression_string] = -1
                    return -1
                left_operand_value = int(expression_string[left_num_start:multiply_index], 2)
                right_operand_value = int(expression_string[multiply_index + 1:right_num_end + 1], 2)
                product = left_operand_value * right_operand_value
                if (left_operand_value < 0 or left_operand_value >= 1024 or
                    right_operand_value < 0 or right_operand_value >= 1024 or
                    product < 0 or product >= 1024):
                    memoized_expressions[expression_string] = -1
                    return -1
                product_binary_str = bin(product)[2:]
                new_expression = expression_string[:left_num_start] + product_binary_str + expression_string[right_num_end + 1:]
                memoized_expressions[expression_string] = evaluate_expression(new_expression)
                return memoized_expressions[expression_string]

            # Addition / Subtraction
            plus_index = INFINITE_INT
            minus_index = INFINITE_INT
            if '+' in expression_string:
                plus_index = expression_string.index('+')
            if '-' in expression_string:
                minus_index = expression_string.index('-')
            if plus_index == INFINITE_INT and minus_index == INFINITE_INT:
                final_value = int(expression_string, 2)
                memoized_expressions[expression_string] = expression_string
                if final_value < 0 or final_value >= 1024:
                    memoized_expressions[expression_string] = -1
                return memoized_expressions[expression_string]
            operator_index = min(plus_index, minus_index)
            left_num_start = operator_index
            for idx in range(operator_index - 1, -1, -1):
                if expression_string[idx] not in '01':
                    break
                left_num_start = idx
            right_num_end = operator_index
            for idx in range(operator_index + 1, expression_length):
                if expression_string[idx] not in '01':
                    break
                right_num_end = idx
            if left_num_start == operator_index or right_num_end == operator_index:
                memoized_expressions[expression_string] = -1
                return -1
            left_operand_value = int(expression_string[left_num_start:operator_index], 2)
            right_operand_value = int(expression_string[operator_index + 1:right_num_end + 1], 2)
            operation_result = left_operand_value + right_operand_value
            if operator_index == minus_index:
                operation_result = left_operand_value - right_operand_value
            if (left_operand_value < 0 or left_operand_value >= 1024 or
                right_operand_value < 0 or right_operand_value >= 1024 or
                operation_result < 0 or operation_result >= 1024):
                memoized_expressions[expression_string] = -1
                return -1
            operation_result_binary_str = bin(operation_result)[2:]
            new_expression = expression_string[:left_num_start] + operation_result_binary_str + expression_string[right_num_end + 1:]
            memoized_expressions[expression_string] = evaluate_expression(new_expression)
            return memoized_expressions[expression_string]

        # Try all permutations of operator combinations inserted between segments
        for inserted_operators_combo in itertools.product(allowed_characters, repeat=num_blocks - 1):
            candidate_expression = ''
            for idx in range(len(inserted_operators_combo)):
                candidate_expression += binary_number_blocks[idx]
                candidate_expression += inserted_operators_combo[idx]
            candidate_expression += binary_number_blocks[-1]
            evaluated_expression = evaluate_expression(candidate_expression)
            numeric_evaluated = -1
            if evaluated_expression != -1:
                numeric_evaluated = int(evaluated_expression, 2)
                if numeric_evaluated >= 1024 or numeric_evaluated < 0:
                    numeric_evaluated = -1
            if maximum_result < numeric_evaluated:
                maximum_result = numeric_evaluated
        return maximum_result

    while True:
        input_string = get_single_string()
        if input_string == '0':
            break
        computed_results.append(compute_maximum_value_by_inserting_operators(input_string))
        break

    return '\n'.join(map(str, computed_results))

print(main())