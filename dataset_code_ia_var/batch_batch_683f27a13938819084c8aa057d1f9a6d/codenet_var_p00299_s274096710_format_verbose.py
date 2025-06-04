import sys
import re
import math
import itertools

def create_edges_between_nodes(from_vertex, to_vertex, edge_weight, sign_indicator):
    """
    Crée les arêtes selon les paramètres, pour gestion des signes et sens.
    """
    edges_list = []

    if sign_indicator == '-':
        edges_list.append((from_vertex, to_vertex, edge_weight if to_vertex else 0))
        edges_list.append((to_vertex, from_vertex, 0))
    else:
        edges_list.append((to_vertex, from_vertex, -edge_weight))

    return edges_list

def bellman_ford_algorithm(edge_list, number_of_vertices):
    """
    Applique l'algorithme de Bellman-Ford pour détecter les cycles de poids négatif
    et calculer la distance max/min à partir du sommet 0.
    Retourne -1 si contrainte impossible, sinon la distance maximale atteignable.
    """
    start_vertex = 0

    shortest_distances = [float('inf')] * number_of_vertices
    shortest_distances[start_vertex] = 0

    for iteration_index in range(number_of_vertices):
        for source_vertex, target_vertex, edge_cost in edge_list:
            if shortest_distances[target_vertex] > shortest_distances[source_vertex] + edge_cost:
                shortest_distances[target_vertex] = shortest_distances[source_vertex] + edge_cost

    for source_vertex, target_vertex, edge_cost in edge_list:
        if shortest_distances[target_vertex] > shortest_distances[source_vertex] + edge_cost:
            return -1

    if min(shortest_distances[1:]) < 0:
        return -1

    return max(shortest_distances)

input_file = sys.stdin

number_of_vertices, number_of_constraints = map(int, input_file.readline().split())

constraint_pattern = re.compile(r'(\d+)(\D+)(\d+)(\D+)(\d+)')
all_constraints_raw = [constraint_pattern.match(line).groups() for line in input_file]

all_fixed_edges = []
all_floating_edges_choices = []

for left_index_str, operator_str, right_index_str, sign_str, weight_str in all_constraints_raw:
    from_node = int(left_index_str) - 1
    to_node = int(right_index_str) - 1
    weight_value = int(weight_str)

    if operator_str == '*':
        if from_node and to_node:
            edges_choice_1 = create_edges_between_nodes(from_node, to_node, weight_value, sign_str)
            edges_choice_2 = create_edges_between_nodes(to_node, from_node, weight_value, sign_str)
            all_floating_edges_choices.append((edges_choice_1, edges_choice_2))
            continue
        operator_str = '<=' if from_node < to_node else '>='

    if operator_str == '>=':
        from_node, to_node = to_node, from_node

    all_fixed_edges.extend(create_edges_between_nodes(from_node, to_node, weight_value, sign_str))

all_possible_distances = []

for floating_edges_variant in itertools.product(*all_floating_edges_choices):
    flattened_edges = [single_edge for edge_group in floating_edges_variant for single_edge in edge_group]
    combined_edge_list = all_fixed_edges + flattened_edges
    distance_result = bellman_ford_algorithm(combined_edge_list, number_of_vertices)
    all_possible_distances.append(distance_result)

print(max(all_possible_distances))