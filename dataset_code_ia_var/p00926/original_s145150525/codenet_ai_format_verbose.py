from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def read_line_as_int_list():
    return list(map(int, sys.stdin.readline().split()))

def read_single_int():
    return int(sys.stdin.readline())

def read_line_as_list_of_lists_of_strings():
    return list(map(list, sys.stdin.readline().split()))

def read_line_as_char_list():
    return list(sys.stdin.readline())[:-1]

def read_n_single_ints(n):
    int_list = [None for _ in range(n)]
    for index in range(n):
        int_list[index] = read_single_int()
    return int_list

def read_n_int_lists(n):
    list_of_int_lists = [None for _ in range(n)]
    for index in range(n):
        list_of_int_lists[index] = read_line_as_int_list()
    return list_of_int_lists

def read_n_lines_as_char_lists(n):
    list_of_char_lists = [None for _ in range(n)]
    for index in range(n):
        list_of_char_lists[index] = read_line_as_char_list()
    return list_of_char_lists

def read_n_lines_as_list_of_lists_of_strings(n):
    list_of_string_lists = [None for _ in range(n)]
    for index in range(n):
        list_of_string_lists[index] = read_line_as_list_of_lists_of_strings()
    return list_of_string_lists

sys.setrecursionlimit(1000000)
MODULO_CONSTANT = 1000000007

def function_A():
    input_expression_string = input()
    expected_result = read_single_int()
    evaluated_expression = eval(input_expression_string)
    first_operand = int(input_expression_string[0])
    length_of_expression = len(input_expression_string)
    if length_of_expression == 1:
        if int(input_expression_string[0]) == expected_result:
            print("U")
        else:
            print("I")
        quit()
    current_operator_is_addition = 0 if input_expression_string[1] == "+" else 1
    for position_in_expression in range(2, length_of_expression):
        if position_in_expression % 2 == 0:
            if current_operator_is_addition:
                first_operand *= int(input_expression_string[position_in_expression])
            else:
                first_operand += int(input_expression_string[position_in_expression])
        else:
            current_operator_is_addition = 0 if input_expression_string[position_in_expression] == "+" else 1
    if evaluated_expression == first_operand:
        if evaluated_expression == expected_result:
            print("U")
        else:
            print("I")
    elif evaluated_expression == expected_result:
        print("M")
    elif first_operand == expected_result:
        print("L")
    else:
        print("I")
    return

def function_B():
    number_of_positions, number_of_requests = read_line_as_int_list()
    visitor_count_delta_at_points = [0 for _ in range(2 * number_of_positions + 3)]

    for request_index in range(number_of_requests):
        start_position, end_position = read_line_as_int_list()
        visitor_count_delta_at_points[2 * start_position] += 1
        visitor_count_delta_at_points[2 * end_position + 1] -= 1

    for index in range(2 * number_of_positions + 1):
        visitor_count_delta_at_points[index + 1] += visitor_count_delta_at_points[index]

    total_unvisited_positions = number_of_positions + 1
    contiguous_visited_sections = 0
    is_in_unvisited_section = 1

    for visitor_count_at_point in visitor_count_delta_at_points:
        if visitor_count_at_point > 0:
            if is_in_unvisited_section:
                is_in_unvisited_section = 0
                contiguous_visited_sections += 1
            total_unvisited_positions += 1
        else:
            is_in_unvisited_section = 1

    total_unvisited_positions -= contiguous_visited_sections
    print(total_unvisited_positions)
    return

def function_C():
    return

def function_D():
    return

def function_E():
    return

def function_F():
    return

def function_G():
    return

def function_H():
    return

def function_I():
    return

def function_J():
    return

if __name__ == "__main__":
    function_B()