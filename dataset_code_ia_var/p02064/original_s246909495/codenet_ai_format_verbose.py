import sys
import math
from collections import defaultdict, deque
from heapq import heappush, heappop
import bisect
import random

def read_integer_list():
    return [int(element) for element in sys.stdin.readline().split()]

def read_single_integer():
    return int(sys.stdin.readline())

def read_list_of_strings():
    return [list(token) for token in sys.stdin.readline().split()]

def read_string_as_list():
    return list(sys.stdin.readline())[:-1]

def read_n_integers(number_of_lines):
    return [read_single_integer() for _ in range(number_of_lines)]

def read_n_integer_lists(number_of_lines):
    return [read_integer_list() for _ in range(number_of_lines)]

def read_n_string_lists(number_of_lines):
    return [read_string_as_list() for _ in range(number_of_lines)]

def read_n_list_of_strings(number_of_lines):
    return [read_list_of_strings() for _ in range(number_of_lines)]

sys.setrecursionlimit(1000000)
MODULO = 1000000007

def problem_A():
    total_steps = read_single_integer()
    cost_per_action = read_integer_list()
    steps_per_action = read_integer_list()
    minimal_total_cost = float('inf')
    for count_first_action in range(total_steps + 1):
        cumulative_steps_after_first = steps_per_action[0] * count_first_action
        cumulative_cost_after_first = cost_per_action[0] * count_first_action
        for count_second_action in range(total_steps + 1):
            cumulative_steps_after_second = cumulative_steps_after_first + steps_per_action[1] * count_second_action
            cumulative_cost_after_second = cumulative_cost_after_first + cost_per_action[1] * count_second_action
            for count_third_action in range(total_steps + 1):
                cumulative_steps_after_third = cumulative_steps_after_second + steps_per_action[2] * count_third_action
                cumulative_cost_after_third = cumulative_cost_after_second + cost_per_action[2] * count_third_action
                remaining_steps = max(0, math.ceil((total_steps - cumulative_steps_after_third) / steps_per_action[3]))
                final_total_cost = cumulative_cost_after_third + cost_per_action[3] * remaining_steps
                if final_total_cost < minimal_total_cost:
                    minimal_total_cost = final_total_cost
    print(minimal_total_cost)
    return

def problem_B():
    def calculate_divisor_product(number):
        if number < 4:
            return 1
        divisor_candidate = 2
        divisor_product = 1
        while divisor_candidate ** 2 <= number:
            if number % divisor_candidate == 0:
                other_divisor = number // divisor_candidate
                if other_divisor != divisor_candidate:
                    divisor_product *= other_divisor
                divisor_product *= divisor_candidate
            divisor_candidate += 1
        return divisor_product

    MAX_RANGE = 100000
    valid_number_flags = [0] * (MAX_RANGE + 1)
    for current_number in range(12, MAX_RANGE + 1):
        if not valid_number_flags[current_number]:
            if calculate_divisor_product(current_number) >= (current_number << 1):
                multiple = current_number
                while multiple <= MAX_RANGE:
                    valid_number_flags[multiple] = 1
                    multiple += current_number
    for index in range(MAX_RANGE):
        valid_number_flags[index + 1] += valid_number_flags[index]
    number_of_queries = read_single_integer()
    for _ in range(number_of_queries):
        print(valid_number_flags[read_single_integer()])
    return

def problem_C():
    def formula(expression_chars, current_index, is_k_flag_set):
        return or_expression(expression_chars, current_index, is_k_flag_set)

    def or_expression(expression_chars, current_index, is_k_flag_set):
        result, next_index = and_expression(expression_chars, current_index, is_k_flag_set)
        while next_index < len(expression_chars) and expression_chars[next_index] == "|":
            next_index += 1
            value, next_index = and_expression(expression_chars, next_index, is_k_flag_set)
            if not is_k_flag_set:
                result += value
        return result, next_index

    def and_expression(expression_chars, current_index, is_k_flag_set):
        term_value, next_index = parse_term(expression_chars, current_index, is_k_flag_set)
        while next_index < len(expression_chars) and expression_chars[next_index] == "&":
            next_index += 1
            value, next_index = parse_term(expression_chars, next_index, is_k_flag_set)
            if is_k_flag_set:
                term_value += value
        return term_value, next_index

    def parse_term(expression_chars, current_index, is_k_flag_set):
        if expression_chars[current_index] == "(":
            current_index += 1
            if not is_k_flag_set:
                or_without_k, new_index = or_expression(expression_chars, current_index, 0)
                or_with_k, current_index = or_expression(expression_chars, current_index, 1)
                return min(or_without_k, or_with_k), current_index + 1
            else:
                or_with_k, current_index = or_expression(expression_chars, current_index, 1)
                return or_with_k, current_index + 1
        return 1, current_index + 1

    input_expression = input()
    print(
        formula(input_expression, 0, 0)[0],
        formula(input_expression, 0, 1)[0]
    )
    return

def problem_D():
    input_first_integer, input_second_integer = read_integer_list()
    for candidate_integer in range(input_second_integer + 1, input_second_integer + input_first_integer):
        temp_result = candidate_integer // input_second_integer
        remainder_after_b = candidate_integer % input_second_integer
        temp_result += remainder_after_b // input_first_integer
        remainder_after_a = remainder_after_b % input_first_integer
        temp_result += remainder_after_a
        summed_division = candidate_integer // input_first_integer + candidate_integer % input_first_integer
        if summed_division < temp_result:
            print(candidate_integer)
            break
    else:
        print(-1)
    return

def problem_E():
    number_of_nodes, source_node, target_node = read_integer_list()
    distance_matrix = [[None] * (number_of_nodes + 1) for _ in range(number_of_nodes + 1)]

    print("?", source_node, target_node)
    print(end='', flush=True)
    shortest_path_distance = read_single_integer()
    distance_matrix[source_node][target_node] = shortest_path_distance
    distance_matrix[target_node][source_node] = shortest_path_distance

    node_info_list = [None] * (number_of_nodes + 1)
    node_info_list[0] = (0, float('inf'))
    node_info_list[source_node] = (source_node, 0)
    node_info_list[target_node] = (target_node, shortest_path_distance)

    for candidate_node in range(1, number_of_nodes + 1):
        if candidate_node in [target_node, source_node]:
            continue

        print("?", source_node, candidate_node)
        print(end='', flush=True)
        distance_from_source = read_single_integer()
        distance_matrix[source_node][candidate_node] = distance_from_source
        distance_matrix[candidate_node][source_node] = distance_from_source

        print("?", candidate_node, target_node)
        print(end='', flush=True)
        distance_to_target = read_single_integer()
        distance_matrix[candidate_node][target_node] = distance_to_target
        distance_matrix[target_node][candidate_node] = distance_to_target

        if distance_from_source + distance_to_target > shortest_path_distance:
            node_info_list[candidate_node] = (candidate_node, float('inf'))
        else:
            node_info_list[candidate_node] = (candidate_node, distance_from_source)

    node_info_list.sort(key=lambda x: x[1])

    for sorted_index in range(number_of_nodes + 1):
        if node_info_list[sorted_index][1] == float('inf'):
            break
    internal_nodes = node_info_list[1:sorted_index - 1]
    number_of_internal_nodes = len(internal_nodes)
    is_on_path = [0] * number_of_internal_nodes

    if is_on_path:
        is_on_path[0] = 1
        previous_node = internal_nodes[0][0]
        for internal_index in range(1, number_of_internal_nodes):
            current_node = internal_nodes[internal_index][0]
            print("?", previous_node, current_node)
            print(end='', flush=True)
            distance_between_nodes = read_single_integer()
            distance_matrix[previous_node][current_node] = distance_between_nodes
            if (
                distance_matrix[source_node][previous_node]
                + distance_between_nodes
                == distance_matrix[source_node][current_node]
            ):
                is_on_path[internal_index] = 1
            else:
                is_on_path[internal_index] = 0

    complete_path = [source_node]
    for internal_index in range(number_of_internal_nodes):
        if is_on_path[internal_index]:
            complete_path.append(internal_nodes[internal_index][0])
    complete_path.append(target_node)

    print("!", *complete_path)
    return

def problem_F():
    number_of_elements = read_single_integer()
    return

def problem_G():
    number_of_vertices, total_weight = read_integer_list()
    weight_list = read_integer_list()
    adjacency_list = [[] for _ in range(number_of_vertices)]
    for edge_index in range(number_of_vertices - 1):
        vertex_a, vertex_b, weight_c = read_integer_list()
        vertex_a -= 1
        vertex_b -= 1
        adjacency_list[vertex_a].append((vertex_b, weight_c))
        adjacency_list[vertex_b].append((vertex_a, weight_c))
    dynamic_programming_list = []
    return

if __name__ == "__main__":
    problem_E()