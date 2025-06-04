from itertools import product, accumulate
from math import gcd
from bisect import bisect
import sys
from sys import setrecursionlimit

setrecursionlimit(10**9)

def read_integers_from_input():
    return list(map(int, input().split()))

def query_distance_between_nodes(node_index_a, node_index_b):
    print("? {} {}".format(node_index_a, node_index_b), end="\n", flush=True)
    return int(input())

number_of_nodes, start_node_index, end_node_index = read_integers_from_input()
distance_between_start_and_end = query_distance_between_nodes(start_node_index, end_node_index)
sorted_distances_list = [0, distance_between_start_and_end]
distance_to_node_index_mapping = {0: start_node_index}
distance_to_node_index_mapping[distance_between_start_and_end] = end_node_index
path_reconstruction_node_list = [start_node_index, end_node_index]

for candidate_node_index in range(1, number_of_nodes + 1):

    if (candidate_node_index == start_node_index) or (candidate_node_index == end_node_index):
        continue

    distance_from_start_to_candidate = query_distance_between_nodes(start_node_index, candidate_node_index)
    distance_from_candidate_to_end = query_distance_between_nodes(candidate_node_index, end_node_index)

    if (distance_from_start_to_candidate * distance_from_candidate_to_end < 0) or \
       (distance_from_start_to_candidate + distance_from_candidate_to_end != distance_between_start_and_end):
        continue

    insertion_index = bisect(sorted_distances_list, distance_from_start_to_candidate) - 1
    prev_distance_value = sorted_distances_list[insertion_index]
    prev_node_index = distance_to_node_index_mapping[prev_distance_value]

    if prev_distance_value == distance_from_start_to_candidate:
        continue

    next_distance_value = sorted_distances_list[insertion_index + 1]
    next_node_index = distance_to_node_index_mapping[next_distance_value]

    distance_from_prev_to_candidate = query_distance_between_nodes(prev_node_index, candidate_node_index)
    distance_from_candidate_to_next = query_distance_between_nodes(candidate_node_index, next_node_index)

    if (prev_distance_value + distance_from_prev_to_candidate +
        distance_from_candidate_to_next + (distance_between_start_and_end - next_distance_value) ==
        distance_between_start_and_end):
        
        distance_to_node_index_mapping[distance_from_start_to_candidate] = candidate_node_index
        path_reconstruction_node_list.insert(insertion_index + 1, candidate_node_index)
        sorted_distances_list.insert(insertion_index + 1, distance_from_start_to_candidate)

print("! " + " ".join(map(str, path_reconstruction_node_list)))