from collections import defaultdict
import sys
read_input_line = lambda: sys.stdin.readline().rstrip()

MODULUS_CONST = 998244353
BASE_CONST = pow(10, 18, MODULUS_CONST)
NUM_NODES = int(read_input_line())

def generate_geometric_sequence_mod(start_value, ratio, modulus, length):
    current_value = start_value
    for index in range(length):
        yield current_value
        current_value = (current_value * ratio) % modulus

geometric_powers = list(generate_geometric_sequence_mod(1, BASE_CONST, MODULUS_CONST, NUM_NODES + 2))

def extended_euclidean_algorithm(val_a, val_b):
    coeff_a1, coeff_b1, remainder1 = 1, 0, val_a
    coeff_a2, coeff_b2, remainder2 = 0, 1, val_b
    while remainder1 != 1:
        quotient, modulo = divmod(remainder2, remainder1)
        coeff_a1, coeff_a2 = coeff_a2 - quotient * coeff_a1, coeff_a1
        coeff_b1, coeff_b2 = coeff_b2 - quotient * coeff_b1, coeff_b1
        remainder1, remainder2 = modulo, remainder1
    return coeff_a1, coeff_b1

def modular_inverse(value_a, value_b, modulus):
    inverse, dummy = extended_euclidean_algorithm(value_a, modulus)
    return (inverse * value_b % modulus)

def minimum_excludant(used_set):
    for candidate in range(NUM_NODES + 1):
        if candidate not in used_set:
            return candidate

def compute_grundy_sum(edge_dict):
    grundy_values = {}
    grundy_sum = defaultdict(int)
    grundy_sum[0] = modular_inverse(BASE_CONST - 1, pow(BASE_CONST, NUM_NODES + 1, MODULUS_CONST) - BASE_CONST, MODULUS_CONST)
    for node_index in range(NUM_NODES, 0, -1):
        if node_index not in edge_dict:
            continue
        reachable_grundies = {grundy_values.get(adj_node, 0) for adj_node in set(edge_dict[node_index])}
        min_excluded_value = minimum_excludant(reachable_grundies)
        if min_excluded_value:
            grundy_values[node_index] = min_excluded_value
            grundy_sum[grundy_values[node_index]] = (grundy_sum[grundy_values[node_index]] + geometric_powers[node_index]) % MODULUS_CONST
            grundy_sum[0] = (grundy_sum[0] - geometric_powers[node_index]) % MODULUS_CONST
    return grundy_sum

def parse_edge_input():
    edge_count = int(read_input_line())
    adjacency_dict = defaultdict(list)
    for edge_index in range(edge_count):
        node_a, node_b = sorted(map(int, read_input_line().split()))
        adjacency_dict[node_a].append(node_b)
    return adjacency_dict

def calculate_total_grundy_value(num_nodes, edge_collections):
    grundy_sums_per_graph = list(map(compute_grundy_sum, edge_collections))
    total_result = 0
    for grundy_x, sum_x in grundy_sums_per_graph[0].items():
        for grundy_y, sum_y in grundy_sums_per_graph[1].items():
            grundy_z = grundy_x ^ grundy_y
            sum_z = grundy_sums_per_graph[2][grundy_z]
            if sum_z:
                total_result = (total_result + sum_x * sum_y * sum_z) % MODULUS_CONST
    return total_result

edge_data_list = [parse_edge_input() for edge_list_index in range(3)]

print(calculate_total_grundy_value(NUM_NODES, edge_data_list))