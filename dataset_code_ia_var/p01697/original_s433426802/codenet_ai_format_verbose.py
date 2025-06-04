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
EPSILON = 1.0 / 10 ** 13
MODULO = 10 ** 9 + 7

FOUR_DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
EIGHT_DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def read_list_of_integers():
    return [int(x) for x in sys.stdin.readline().split()]

def read_list_of_integers_minus_one():
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

def print_and_flush(output):
    return print(output, flush=True)

def main():
    list_of_results = []
    
    def solve_single_case(num_nodes, num_edges, max_height, num_special_keys):
        graph = collections.defaultdict(list)
        for _ in range(num_edges):
            from_node, to_node, cost, height_required, required_key = read_list_of_integers()
            graph[from_node].append((to_node, cost, height_required, required_key))
            graph[to_node].append((from_node, cost, height_required, required_key))
        
        start_node, end_node = read_list_of_integers()
        num_potions = read_single_integer()
        potion_list = []
        bit_masks = [2 ** i for i in range(num_special_keys + 1)]
        
        for _ in range(num_potions):
            potion_data = read_list_of_integers()
            potion_cost = potion_data[1]
            potion_keys_bitmask = 0
            for key_index in potion_data[2:]:
                potion_keys_bitmask += bit_masks[key_index]
            potion_list.append((potion_keys_bitmask, potion_cost))
        
        minimum_cost_with_bitmask = collections.defaultdict(lambda: INFINITY)
        minimum_cost_with_bitmask[0] = 0
        
        for current_keys_bitmask, current_potion_cost in potion_list:
            current_bitmask_cost_items = list(minimum_cost_with_bitmask.items())
            for used_keys_bitmask, used_total_cost in current_bitmask_cost_items:
                combined_keys_bitmask = current_keys_bitmask | used_keys_bitmask
                combined_total_cost = used_total_cost + current_potion_cost
                if minimum_cost_with_bitmask[combined_keys_bitmask] > combined_total_cost:
                    minimum_cost_with_bitmask[combined_keys_bitmask] = combined_total_cost
        
        overall_minimum_total_cost = INFINITY
        
        for used_keys_bitmask, total_potions_cost in minimum_cost_with_bitmask.items():
            unlocked_key_indices = set()
            if total_potions_cost >= overall_minimum_total_cost:
                continue
            for key_idx in range(num_special_keys + 1):
                if used_keys_bitmask & bit_masks[key_idx]:
                    unlocked_key_indices.add(key_idx)
            
            def shortest_path_search():
                distance = collections.defaultdict(lambda: INFINITY)
                distance[(start_node, 0)] = 0
                priority_queue = []
                heapq.heappush(priority_queue, (0, (start_node, 0)))
                visited = collections.defaultdict(bool)
                
                while len(priority_queue):
                    current_total_cost, (current_node, accumulated_height) = heapq.heappop(priority_queue)
                    if visited[(current_node, accumulated_height)]:
                        continue
                    visited[(current_node, accumulated_height)] = True
                    if current_node == end_node:
                        return current_total_cost
                    for neighbor_node, edge_cost, edge_height_required, edge_required_key in graph[current_node]:
                        new_accumulated_height = accumulated_height + edge_height_required
                        if new_accumulated_height > max_height:
                            continue
                        next_state = (neighbor_node, new_accumulated_height)
                        if visited[next_state]:
                            continue
                        next_total_cost = current_total_cost
                        if edge_required_key not in unlocked_key_indices:
                            next_total_cost += edge_cost
                        if distance[next_state] > next_total_cost:
                            distance[next_state] = next_total_cost
                            heapq.heappush(priority_queue, (next_total_cost, next_state))
                return INFINITY

            minimum_path_cost = shortest_path_search()
            if overall_minimum_total_cost > minimum_path_cost + total_potions_cost:
                overall_minimum_total_cost = minimum_path_cost + total_potions_cost
            if overall_minimum_total_cost == INFINITY:
                break
        
        if overall_minimum_total_cost == INFINITY:
            return -1
        
        return overall_minimum_total_cost
    
    while True:
        num_nodes, num_edges, max_height, num_special_keys = read_list_of_integers()
        if num_nodes == 0:
            break
        case_result = solve_single_case(num_nodes, num_edges, max_height, num_special_keys)
        list_of_results.append(case_result)
    
    return '\n'.join(map(str, list_of_results))

print(main())