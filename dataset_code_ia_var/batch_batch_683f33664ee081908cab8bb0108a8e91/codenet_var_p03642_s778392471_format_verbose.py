import itertools
from math import sqrt

def group_consecutive_integers(input_list):
    current_index = 0
    grouped_list = []
    while current_index < len(input_list):
        grouped_list.append(input_list[current_index])
        while current_index != (len(input_list) - 1) and input_list[current_index + 1] == input_list[current_index] + 1:
            current_index += 1
        grouped_list.append(input_list[current_index] + 1)
        current_index += 1
    return grouped_list

def find_augmenting_path_and_update_graph(graph, source_node, target_node):
    parent_nodes = [None] * len(graph)
    path_candidates = [(source_node, source_node)]

    while path_candidates:
        current_node, parent_node = path_candidates.pop()
        if parent_nodes[current_node] is None:
            parent_nodes[current_node] = parent_node
            for adjacent_node in graph[current_node]:
                if parent_nodes[adjacent_node] is None:
                    path_candidates.append((adjacent_node, current_node))
    if not parent_nodes[target_node]:
        return False

    traversed_node = target_node
    while traversed_node != source_node:
        graph[parent_nodes[traversed_node]].discard(traversed_node)
        graph[traversed_node].add(parent_nodes[traversed_node])
        traversed_node = parent_nodes[traversed_node]

    return True

def maximum_matching(edge_list):
    node_label_to_index = {}
    next_index = 0
    total_matches = 0

    for node_left, node_right in edge_list:
        if node_left not in node_label_to_index:
            node_label_to_index[node_left] = next_index
            next_index += 1
        if node_right not in node_label_to_index:
            node_label_to_index[node_right] = next_index
            next_index += 1

    index_to_node_label = {index: label for label, index in node_label_to_index.items()}
    adjacency_list = [set() for _ in range(len(node_label_to_index) + 2)]
    source_index = len(node_label_to_index)
    target_index = source_index + 1

    for node_left, node_right in edge_list:
        adjacency_list[source_index].add(node_label_to_index[node_left])
        adjacency_list[node_label_to_index[node_left]].add(node_label_to_index[node_right])
        adjacency_list[node_label_to_index[node_right]].add(target_index)

    while find_augmenting_path_and_update_graph(adjacency_list, source_index, target_index):
        total_matches += 1
    return total_matches

def is_prime(candidate_integer):
    if candidate_integer <= 1:
        return False
    for divisor in range(2, min(candidate_integer, int(sqrt(candidate_integer) + 7))):
        if candidate_integer % divisor == 0:
            return False
    return True

def generate_eligible_pairs(integer_list):
    eligible_pairs = []
    for even_integer in integer_list:
        for odd_integer in integer_list:
            if even_integer % 2 == 0 and odd_integer % 2 == 1 and is_prime(abs(even_integer - odd_integer)):
                eligible_pairs.append((even_integer, odd_integer))
    return eligible_pairs

number_of_input_elements = int(input())
integer_input_values = list(map(int, input().split()))
consecutive_grouped_integers = group_consecutive_integers(integer_input_values)
possible_pairs = generate_eligible_pairs(consecutive_grouped_integers)
maximum_pairings = maximum_matching(possible_pairs)

number_of_even_integers = len(list(filter(lambda value: value % 2 == 0, consecutive_grouped_integers)))
number_of_odd_integers = len(consecutive_grouped_integers) - number_of_even_integers

pairings_not_used_even = number_of_even_integers - maximum_pairings
pairings_not_used_odd = number_of_odd_integers - maximum_pairings

final_result = int(
    maximum_pairings
    + 2 * ((pairings_not_used_even // 2) + (pairings_not_used_odd // 2))
    + 3 * ((pairings_not_used_even % 2))
)

print(final_result)