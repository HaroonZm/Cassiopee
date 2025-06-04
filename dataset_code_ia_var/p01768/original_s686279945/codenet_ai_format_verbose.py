INFINITY_COST = 10**9

parent_indices = [0] * 5001
tree_ranks = [0] * 5001

def initialize_union_find(number_of_vertices):
    for vertex_index in xrange(number_of_vertices):
        parent_indices[vertex_index] = vertex_index
        tree_ranks[vertex_index] = 0

def find_set(node_index):
    if parent_indices[node_index] == node_index:
        return node_index
    else:
        parent_indices[node_index] = find_set(parent_indices[node_index])
        return parent_indices[node_index]

def union_sets(first_index, second_index):
    root_first = find_set(first_index)
    root_second = find_set(second_index)
    if root_first == root_second:
        return

    if tree_ranks[root_first] < tree_ranks[root_second]:
        parent_indices[root_first] = root_second
    else:
        parent_indices[root_second] = root_first
        if tree_ranks[root_first] == tree_ranks[root_second]:
            tree_ranks[root_first] += 1

def are_in_same_set(first_index, second_index):
    return find_set(first_index) == find_set(second_index)

number_of_nodes = int(raw_input())
initialize_union_find(number_of_nodes)

node_costs = [0] * number_of_nodes
name_to_index = {}

for node_iterator in xrange(number_of_nodes):
    node_name, node_cost_string = raw_input().split()
    name_to_index[node_name] = node_iterator
    node_costs[node_iterator] = int(node_cost_string)

number_of_unions = int(raw_input())
for union_operation_counter in xrange(number_of_unions):
    source_name, target_name = raw_input().split()
    union_sets(name_to_index[source_name], name_to_index[target_name])

total_cost = 0
representative_min_cost = [INFINITY_COST] * number_of_nodes

sorted_node_costs = sorted(enumerate(node_costs), key=lambda pair: pair[1])

for node_index, cost_value in sorted_node_costs:
    set_representative = find_set(node_index)
    if representative_min_cost[set_representative] == INFINITY_COST:
        representative_min_cost[set_representative] = cost_value
    total_cost += representative_min_cost[set_representative]

print total_cost