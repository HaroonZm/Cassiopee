#!/usr/bin/env python3

import sys
import math
import bisect
import random
import itertools
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop

sys.setrecursionlimit(10 ** 5)

standard_input_stream = sys.stdin

bisect_left_function = bisect.bisect_left
bisect_right_function = bisect.bisect_right

def read_int_list():
    return list(map(int, standard_input_stream.readline().split()))

def read_float_list():
    return list(map(float, standard_input_stream.readline().split()))

def read_zero_based_int_list():
    return list(map(lambda x: int(x) - 1, standard_input_stream.readline().split()))

def read_single_int():
    return int(standard_input_stream.readline())

def read_single_float():
    return float(standard_input_stream.readline())

def read_list_of_strings():
    return list(map(list, standard_input_stream.readline().split()))

def read_string_as_char_list():
    return list(standard_input_stream.readline().rstrip())

def read_n_integers(number_of_lines):
    return [read_single_int() for _ in range(number_of_lines)]

def read_n_lists_of_ints(number_of_lines):
    return [read_int_list() for _ in range(number_of_lines)]

def read_n_floats(number_of_lines):
    return [read_single_float() for _ in range(number_of_lines)]

def read_n_lists_of_floats(number_of_lines):
    return [read_float_list() for _ in range(number_of_lines)]

def read_n_zero_based_lists_of_ints(number_of_lines):
    return [read_zero_based_int_list() for _ in range(number_of_lines)]

def read_n_strings_as_char_lists(number_of_lines):
    return [read_string_as_char_list() for _ in range(number_of_lines)]

def read_n_lists_of_strings(number_of_lines):
    return [read_list_of_strings() for _ in range(number_of_lines)]

MODULO_CONSTANT = 1000000007
INFINITY_FLOAT = float('INF')


# Problem A
def problem_a_minimum_cost_dp():
    target_sum = read_single_int()
    price_list = read_int_list()
    time_list = read_int_list()

    dynamic_programming_min_cost = [INFINITY_FLOAT] * (10 ** 5)
    dynamic_programming_min_cost[0] = 0

    for current_time in range(10 ** 5):
        for index_of_option, required_time in enumerate(time_list):
            if current_time - required_time >= 0:
                dynamic_programming_min_cost[current_time] = min(
                    dynamic_programming_min_cost[current_time],
                    dynamic_programming_min_cost[current_time - required_time] + price_list[index_of_option]
                )

    for current_time in range(10 ** 5 - 1, 0, -1):
        dynamic_programming_min_cost[current_time - 1] = min(
            dynamic_programming_min_cost[current_time],
            dynamic_programming_min_cost[current_time - 1]
        )

    print(dynamic_programming_min_cost[target_sum])
    return


# Problem B
def problem_b_divisor_count():
    def count_divisors(upto_number):
        divisor_count = 0
        if upto_number == 0:
            return 0
        for possible_divisor in range(1, int(math.sqrt(upto_number - 1)) + 1):
            if upto_number % possible_divisor == 0:
                divisor_count += 2
        if float.is_integer(math.sqrt(upto_number)):
            divisor_count += 1
        return divisor_count

    number_of_queries = read_single_int()
    divisor_counts_accumulated = [count_divisors(number) for number in range(10 ** 5 + 1)]
    divisor_counts_accumulated[0] = 0

    for i in range(1, 10 ** 5 + 1):
        if divisor_counts_accumulated[i] >= 5:
            divisor_counts_accumulated[i] = 1
        else:
            divisor_counts_accumulated[i] = 0
        divisor_counts_accumulated[i] += divisor_counts_accumulated[i - 1]

    for _ in range(number_of_queries):
        query_number = read_single_int()
        print(divisor_counts_accumulated[query_number])
    return


# Problem C (empty)
def problem_c():
    return


# Problem D
def problem_d_math_check():
    first_integer, second_integer = read_int_list()

    if second_integer % first_integer == 0 or first_integer == 2:
        print(-1)
    else:
        quotient_value = second_integer // first_integer + 1
        candidate_value = first_integer * quotient_value
        if quotient_value < candidate_value // second_integer + candidate_value % second_integer:
            print(candidate_value)
        else:
            print(-1)
    return


# Problem E
def problem_e_interactive_path_reconstruction():
    number_of_nodes, source_node, target_node = read_int_list()
    shortest_distance_map = defaultdict(lambda: INFINITY_FLOAT)

    print("?", source_node, target_node, flush=True)
    initial_distance = read_single_int()
    shortest_distance_map[(target_node, source_node)] = initial_distance
    shortest_distance_map[(source_node, target_node)] = initial_distance

    candidate_nodes_with_distances = []

    for current_node in range(1, number_of_nodes + 1):

        if current_node == source_node or current_node == target_node:
            continue

        print("?", source_node, current_node, flush=True)
        distance_from_source = read_single_int()
        shortest_distance_map[(source_node, current_node)] = distance_from_source
        shortest_distance_map[(current_node, source_node)] = distance_from_source

        print("?", target_node, current_node, flush=True)
        distance_from_target = read_single_int()
        shortest_distance_map[(target_node, current_node)] = distance_from_target
        shortest_distance_map[(current_node, target_node)] = distance_from_target

        if distance_from_source + distance_from_target == shortest_distance_map[(source_node, target_node)]:
            shortest_distance_map[(source_node, target_node)] = distance_from_source + distance_from_target
            candidate_nodes_with_distances.append((current_node, distance_from_source))

    if not candidate_nodes_with_distances:
        print("!", source_node, target_node, flush=True)
        return

    candidate_nodes_with_distances.sort(key=lambda pair: pair[1])
    closest_node = candidate_nodes_with_distances[0][0]
    reconstructed_path = [source_node, closest_node]

    for next_candidate_node, _ in candidate_nodes_with_distances[1:]:
        print("?", closest_node, next_candidate_node, flush=True)
        distance_between_candidates = read_single_int()
        if (shortest_distance_map[(source_node, closest_node)] +
            distance_between_candidates == shortest_distance_map[(source_node, next_candidate_node)]):
            reconstructed_path.append(next_candidate_node)

    reconstructed_path.append(target_node)

    print("!", *reconstructed_path, flush=True)

    return


# Problem F (empty)
def problem_f():
    return

# Problem G (empty)
def problem_g():
    return

# Problem H (empty)
def problem_h():
    return


# Main solve invocation
if __name__ == '__main__':
    problem_e_interactive_path_reconstruction()