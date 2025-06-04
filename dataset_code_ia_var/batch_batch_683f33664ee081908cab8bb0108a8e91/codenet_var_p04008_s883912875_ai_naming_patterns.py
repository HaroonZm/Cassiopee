import sys
import copy
import bisect
import itertools
import heapq
import math
from heapq import heappop, heappush, heapify
from collections import Counter, defaultdict, deque

def input_int():
    return int(sys.stdin.readline())

def input_int_list():
    return list(map(int, sys.stdin.readline().split()))

def input_float_list():
    return list(map(float, sys.stdin.readline().split()))

def input_str_list():
    return list(map(str, sys.stdin.readline().split()))

def input_str_split():
    return sys.stdin.readline().split()

def input_str():
    return sys.stdin.readline().strip()

MOD_1 = 10**9 + 7
MOD_2 = 998244353
INF = 10**18
ALPHABET = [chr(ord('a') + idx) for idx in range(26)]

sys.setrecursionlimit(10**6)

def process_problem_a():
    value_a, value_b, value_c = input_int_list()
    min_result = min(
        value_a * value_b * (value_c % 2),
        value_a * value_c * (value_b % 2),
        value_b * value_c * (value_a % 2)
    )
    print(min_result)
    return

def process_problem_b():
    class SegmentTree:
        def __init__(self, array_data, array_size, function_segment):
            self.identity_element = INF
            self.length_exponent = 1 << (array_size - 1).bit_length()
            self.tree_array = [self.identity_element] * (2 * self.length_exponent)
            self.segment_function = function_segment
            for idx in range(array_size):
                self.tree_array[idx + self.length_exponent] = array_data[idx]
            for idx in range(self.length_exponent - 1, 0, -1):
                self.tree_array[idx] = self.segment_function(
                    self.tree_array[2 * idx], self.tree_array[2 * idx + 1]
                )
        def set_value(self, position, replacement):
            position += self.length_exponent
            self.tree_array[position] = replacement
            while position:
                position >>= 1
                self.tree_array[position] = self.segment_function(
                    self.tree_array[2 * position], self.tree_array[2 * position + 1]
                )
        def increment_value(self, position):
            position += self.length_exponent
            self.tree_array[position] += 1
            while position:
                position >>= 1
                self.tree_array[position] = self.segment_function(
                    self.tree_array[2 * position], self.tree_array[2 * position + 1]
                )
        def decrement_value(self, position):
            position += self.length_exponent
            self.tree_array[position] -= 1
            while position:
                position >>= 1
                self.tree_array[position] = self.segment_function(
                    self.tree_array[2 * position], self.tree_array[2 * position + 1]
                )
        def get_range_result(self, range_left, range_right):
            if range_right < range_left:
                return self.identity_element
            range_left += self.length_exponent
            range_right += self.length_exponent
            result_value = self.identity_element
            while range_left < range_right:
                if range_left & 1:
                    result_value = self.segment_function(result_value, self.tree_array[range_left])
                    range_left += 1
                if range_right & 1:
                    range_right -= 1
                    result_value = self.segment_function(result_value, self.tree_array[range_right])
                range_left >>= 1
                range_right >>= 1
            return result_value

    total_elements, add_cost = input_int_list()
    input_array = input_int_list()
    segment_tree_min = SegmentTree(input_array, total_elements, lambda arg1, arg2: min(arg1, arg2))
    complete_result = INF
    for rotate_offset in range(total_elements):
        current_sum = 0
        for position in range(total_elements):
            if position - rotate_offset >= 0:
                minimal_value = segment_tree_min.get_range_result(position - rotate_offset, position + 1)
            else:
                minimal_value = min(
                    segment_tree_min.get_range_result(0, position + 1),
                    segment_tree_min.get_range_result(total_elements - (rotate_offset - position), total_elements)
                )
            current_sum += minimal_value
        complete_result = min(complete_result, current_sum + rotate_offset * add_cost)
    print(complete_result)
    return

def process_problem_c():
    num_rows, num_cols = input_int_list()
    data_matrix = [input_str() for _ in range(num_rows)]
    output_result = 0
    print(output_result)
    return

def process_problem_d():
    num_nodes, path_length = input_int_list()
    node_values = input_int_list()
    adjacency_list = [[] for _ in range(num_nodes)]
    result_count = 0
    if node_values[0] != 1:
        result_count += 1
        node_values[0] = 1
    for current_index in range(1, num_nodes):
        adjacency_list[node_values[current_index] - 1].append(current_index)
    def depth_first_search(parent_index, current_index):
        current_depth = 0
        node_count = 0
        for child_index in adjacency_list[current_index]:
            sub_depth, sub_count = depth_first_search(current_index, child_index)
            current_depth = max(current_depth, sub_depth)
            node_count += sub_count
        current_depth += 1
        if current_depth == path_length and parent_index != 0:
            current_depth = 0
            node_count += 1
        return current_depth, node_count
    _, total_count = depth_first_search(0, 0)
    result_count += total_count
    print(result_count)
    return

def process_problem_e():
    return_value = 0
    print(return_value)
    return

def process_problem_f():
    output_value = 0
    print(output_value)
    return

if __name__ == '__main__':
    process_problem_d()