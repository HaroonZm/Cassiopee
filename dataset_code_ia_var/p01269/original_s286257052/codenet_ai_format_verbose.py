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

INFINITY = 10 ** 20
EPSILON = 1.0 / 10 ** 10
MODULO = 10 ** 9 + 7

FOUR_DIRECTION_OFFSETS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

EIGHT_DIRECTION_OFFSETS = [
    (-1, 0), (-1, 1), (0, 1), (1, 1),
    (1, 0), (1, -1), (0, -1), (-1, -1)
]

def read_int_list():
    return [int(element) for element in sys.stdin.readline().split()]

def read_zero_based_int_list():
    return [int(element) - 1 for element in sys.stdin.readline().split()]

def read_float_list():
    return [float(element) for element in sys.stdin.readline().split()]

def read_string_list():
    return sys.stdin.readline().split()

def read_single_int():
    return int(sys.stdin.readline())

def read_single_float():
    return float(sys.stdin.readline())

def read_single_line():
    return input()

def print_flush(value):
    print(value, flush=True)

def main():
    all_results = []

    def find_minimal_cost(
        number_of_nodes,
        number_of_edges,
        capacity_limit
    ):
        adjacency_list = collections.defaultdict(list)

        for _ in range(number_of_edges):
            start_node, end_node, add_capacity, add_cost = read_int_list()
            adjacency_list[start_node].append((end_node, add_capacity, add_cost))
            adjacency_list[end_node].append((start_node, add_capacity, add_cost))

        minimal_cost_per_state = collections.defaultdict(lambda: INFINITY)
        minimal_cost_per_state[(1, 0)] = 0

        priority_queue = []
        heapq.heappush(priority_queue, (0, 0, 1))

        visited_state = collections.defaultdict(bool)
        minimal_result = INFINITY

        while priority_queue:
            current_total_cost, current_capacity, current_node = heapq.heappop(priority_queue)

            if visited_state[(current_node, current_capacity)]:
                continue

            visited_state[(current_node, current_capacity)] = True

            if current_node == number_of_nodes and minimal_result > current_total_cost:
                minimal_result = current_total_cost

            for neighbor_node, capacity_increase, cost_increase in adjacency_list[current_node]:
                next_capacity = current_capacity + capacity_increase
                next_state = (neighbor_node, next_capacity)

                if not visited_state[next_state] and next_capacity <= capacity_limit:
                    next_cost = current_total_cost

                    if minimal_cost_per_state[next_state] > next_cost:
                        minimal_cost_per_state[next_state] = next_cost
                        heapq.heappush(priority_queue, (next_cost, next_capacity, neighbor_node))

                alternative_state = (neighbor_node, current_capacity)

                if not visited_state[alternative_state]:
                    alternative_cost = current_total_cost + cost_increase

                    if minimal_cost_per_state[alternative_state] > alternative_cost:
                        minimal_cost_per_state[alternative_state] = alternative_cost
                        heapq.heappush(priority_queue, (alternative_cost, current_capacity, neighbor_node))

        return minimal_result

    while True:
        node_count, edge_count, limit_capacity = read_int_list()
        if node_count == 0 and edge_count == 0:
            break
        all_results.append(
            find_minimal_cost(
                node_count,
                edge_count,
                limit_capacity
            )
        )

    return '\n'.join(map(str, all_results))

print(main())