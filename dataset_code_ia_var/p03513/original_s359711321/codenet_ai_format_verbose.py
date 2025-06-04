import sys
import numpy as np
import numba
from numba import njit, i8

MODULUS = 1_000_000_007

input_buffer = sys.stdin.buffer

def read_input_line():
    return input_buffer.readline()

def read_input_lines():
    return input_buffer.readlines()

@njit((i8, i8[:, :]), cache=True)
def count_spanning_configurations(num_nodes, adjacency_matrix):
    # Precompute powers of 2 modulo the modulus up to 1000
    power_of_two_mod = np.empty(1000, np.int64)
    power_of_two_mod[0] = 1
    for index in range(1, 1000):
        power_of_two_mod[index] = power_of_two_mod[index - 1] * 2 % MODULUS

    # For every subset, store the number of edges contained in the subset
    edge_count_for_subset = np.zeros(1 << num_nodes, np.int64)
    for node_b in range(num_nodes):
        for node_a in range(node_b):
            if adjacency_matrix[node_a, node_b]:
                current_subset = (1 << node_a) | (1 << node_b)
                edge_count_for_subset[current_subset] += 1

    # Use DP to count all edges present in every subset
    for bit_index in range(num_nodes):
        for subset_mask in range(1 << num_nodes):
            expanded_subset = subset_mask | (1 << bit_index)
            if subset_mask == expanded_subset:
                continue
            edge_count_for_subset[expanded_subset] += edge_count_for_subset[subset_mask]

    # dp_starting_from_zero[subset]: number of ways to move over all nodes in `subset` starting from node 0
    dp_starting_from_zero = np.zeros(1 << num_nodes, np.int64)
    for subset_mask in range(1 << num_nodes):
        if (subset_mask & 1) == 0:
            continue
        total_ways = power_of_two_mod[edge_count_for_subset[subset_mask]]
        subsubset_mask = subset_mask
        while subsubset_mask:
            subsubset_mask = (subsubset_mask - 1) & subset_mask
            if (subsubset_mask & 1) == 0:
                continue
            dp_value = dp_starting_from_zero[subsubset_mask]
            edge_count_only_in_remaining = edge_count_for_subset[subset_mask ^ subsubset_mask]
            inside_edges = edge_count_for_subset[subset_mask] - edge_count_for_subset[subsubset_mask] - edge_count_only_in_remaining
            dp_value = dp_value * power_of_two_mod[edge_count_only_in_remaining] % MODULUS
            total_ways -= dp_value
        dp_starting_from_zero[subset_mask] = total_ways % MODULUS

    # dp_starting_from_one[subset]: number of ways to move over all nodes in `subset` starting from node 1
    dp_starting_from_one = np.zeros(1 << num_nodes, np.int64)
    for subset_mask in range(1 << num_nodes):
        if (subset_mask & 2) == 0:
            continue
        total_ways = power_of_two_mod[edge_count_for_subset[subset_mask]]
        subsubset_mask = subset_mask
        while subsubset_mask:
            subsubset_mask = (subsubset_mask - 1) & subset_mask
            if (subsubset_mask & 2) == 0:
                continue
            dp_value = dp_starting_from_one[subsubset_mask]
            edge_count_only_in_remaining = edge_count_for_subset[subset_mask ^ subsubset_mask]
            inside_edges = edge_count_for_subset[subset_mask] - edge_count_for_subset[subsubset_mask] - edge_count_only_in_remaining
            dp_value = dp_value * power_of_two_mod[edge_count_only_in_remaining] % MODULUS
            total_ways -= dp_value
        dp_starting_from_one[subset_mask] = total_ways % MODULUS

    # Calculate the answer on the basis of separated traversals from nodes 0 and 1
    full_set_mask = (1 << num_nodes) - 1
    result = power_of_two_mod[edge_count_for_subset[full_set_mask]]

    for reachable_from_zero_mask in range(1 << num_nodes):
        complement_mask = full_set_mask ^ reachable_from_zero_mask
        if (reachable_from_zero_mask & 1) == 0:
            continue
        if (complement_mask & 2) == 0:
            continue
        submask_in_complement = complement_mask + 1
        while submask_in_complement:
            submask_in_complement = (submask_in_complement - 1) & complement_mask
            if (submask_in_complement & 2):
                unreachable_mask = full_set_mask ^ reachable_from_zero_mask ^ submask_in_complement
                number_of_edges_between_two_parts = edge_count_for_subset[reachable_from_zero_mask | submask_in_complement] - edge_count_for_subset[reachable_from_zero_mask] - edge_count_for_subset[submask_in_complement]
                if number_of_edges_between_two_parts:
                    continue
                total_configurations = dp_starting_from_zero[reachable_from_zero_mask] * dp_starting_from_one[submask_in_complement] % MODULUS
                total_configurations = total_configurations * power_of_two_mod[edge_count_for_subset[unreachable_mask]] % MODULUS
                result -= total_configurations

    return result % MODULUS

# Parse the input graph
number_of_nodes, number_of_edges = map(int, read_input_line().split())
adjacency_matrix = np.zeros((number_of_nodes, number_of_nodes), np.int64)

for _ in range(number_of_edges):
    node_from, node_to = map(int, read_input_line().split())
    node_from -= 1
    node_to -= 1
    adjacency_matrix[node_from, node_to] = 1
    adjacency_matrix[node_to, node_from] = 1

print(count_spanning_configurations(number_of_nodes, adjacency_matrix))