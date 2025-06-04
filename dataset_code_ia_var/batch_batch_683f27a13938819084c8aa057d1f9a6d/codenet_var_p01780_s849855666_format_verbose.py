import sys

import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import random
import time
import copy
import functools

# Augmenter la limite de récursivité pour les appels profonds
sys.setrecursionlimit(10 ** 7)

INFINITY_LARGE = 10 ** 20
FLOATING_POINT_EPSILON = 1.0 / 10 ** 13
MODULO_LARGE_PRIME = 10 ** 9 + 7

CARDINAL_DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ALL_EIGHT_DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def read_list_of_integers():
    return [int(x) for x in sys.stdin.readline().split()]

def read_list_of_integers_zero_based():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def read_list_of_floats():
    return [float(x) for x in sys.stdin.readline().split()]

def read_list_of_strings():
    return sys.stdin.readline().split()

def read_single_integer():
    return int(sys.stdin.readline())

def read_single_float():
    return float(sys.stdin.readline())

def read_single_string():
    return input()

def print_and_flush(output_string):
    print(output_string, flush=True)

def main():

    number_of_nodes = read_single_integer()

    if number_of_nodes == 1:
        return 0

    parent_list_zero_based = read_list_of_integers_zero_based()

    depth_list_for_each_node = [0]
    binary_lifting_table = [[None] * 18]

    # Remplissage des parents et profondeur avec binary lifting
    for current_node_index in range(number_of_nodes - 1):

        parent_index = parent_list_zero_based[current_node_index]

        depth_list_for_each_node.append(
            depth_list_for_each_node[parent_index] + 1
        )

        ancestor_list = [None] * 18
        ancestor_list[0] = parent_index

        for pow2_step in range(1, 18):
            previous_ancestor = ancestor_list[pow2_step - 1]
            if binary_lifting_table[previous_ancestor][pow2_step - 1] is None:
                break
            ancestor_list[pow2_step] = binary_lifting_table[previous_ancestor][pow2_step - 1]

        binary_lifting_table.append(ancestor_list)

    powers_of_two = [2 ** exp for exp in range(19)]

    def calculate_distance_between_nodes(node_index_a, node_index_b):

        if node_index_a == node_index_b:
            return 0

        if depth_list_for_each_node[node_index_a] > depth_list_for_each_node[node_index_b]:
            depth_difference = depth_list_for_each_node[node_index_a] - depth_list_for_each_node[node_index_b]
            for binary_step in range(1, 18):
                if depth_difference < powers_of_two[binary_step]:
                    ancestor_target = binary_lifting_table[node_index_a][binary_step - 1]
                    distance_rest = calculate_distance_between_nodes(ancestor_target, node_index_b)
                    return powers_of_two[binary_step - 1] + distance_rest

        if depth_list_for_each_node[node_index_a] < depth_list_for_each_node[node_index_b]:
            depth_difference = depth_list_for_each_node[node_index_b] - depth_list_for_each_node[node_index_a]
            for binary_step in range(1, 18):
                if depth_difference < powers_of_two[binary_step]:
                    ancestor_target = binary_lifting_table[node_index_b][binary_step - 1]
                    distance_rest = calculate_distance_between_nodes(ancestor_target, node_index_a)
                    return powers_of_two[binary_step - 1] + distance_rest

        for binary_step in range(1, 18):
            if binary_lifting_table[node_index_a][binary_step] == binary_lifting_table[node_index_b][binary_step]:
                ancestor_a = binary_lifting_table[node_index_a][binary_step - 1]
                ancestor_b = binary_lifting_table[node_index_b][binary_step - 1]
                distance_rest = calculate_distance_between_nodes(ancestor_a, ancestor_b)
                return powers_of_two[binary_step] + distance_rest

    # Trie des sommets par profondeur puis par indice
    combined_depth_and_index_list = sorted(
        zip(depth_list_for_each_node, range(number_of_nodes))
    )

    traversal_order_node_indices = [0]
    node_index_to_position_in_traversal_order = {}
    node_index_to_position_in_traversal_order[0] = 0

    traversal_iterator = 1

    while traversal_iterator < number_of_nodes:

        next_level_last_index = traversal_iterator + 1
        current_depth = combined_depth_and_index_list[traversal_iterator][0]

        while (
            next_level_last_index < number_of_nodes
            and combined_depth_and_index_list[next_level_last_index][0] == current_depth
        ):
            next_level_last_index += 1

        # Trie des noeuds au même niveau selon le parent
        sorted_current_level = sorted(
            [
                [node_index_to_position_in_traversal_order[binary_lifting_table[node][0]], node]
                for _, node in combined_depth_and_index_list[traversal_iterator:next_level_last_index]
            ]
        )

        traversal_order_node_indices.extend(
            list(map(lambda item: item[1], sorted_current_level))
        )

        for k in range(traversal_iterator, next_level_last_index):
            idx_in_traversal_order = k
            node_position = traversal_order_node_indices[idx_in_traversal_order]
            node_index_to_position_in_traversal_order[node_position] = idx_in_traversal_order

        traversal_iterator = next_level_last_index

    total_distance_accumulated = 1

    for node_in_sequence_index in range(1, number_of_nodes - 1):
        node_u = traversal_order_node_indices[node_in_sequence_index]
        node_v = traversal_order_node_indices[node_in_sequence_index + 1]
        total_distance_accumulated += calculate_distance_between_nodes(node_u, node_v)

    return total_distance_accumulated

print(main())