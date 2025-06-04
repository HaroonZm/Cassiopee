import sys

read_input_line = sys.stdin.readline

segment_tree_length, number_of_queries = map(int, read_input_line().split())

segment_tree_element_count = 1 << (segment_tree_length.bit_length())
segment_tree_height = 1 + segment_tree_length.bit_length()

segment_tree_nodes = [0] * (2 * segment_tree_element_count)
segment_tree_lazy = [None] * (2 * segment_tree_element_count)

def get_propagate_indexes(left_index, right_index):
    propagate_node_indexes = []

    right_index -= 1

    left_index >>= 1
    right_index >>= 1

    while left_index != right_index:
        if left_index > right_index:
            propagate_node_indexes.append(left_index)
            left_index >>= 1
        else:
            propagate_node_indexes.append(right_index)
            right_index >>= 1

    while left_index != 0:
        propagate_node_indexes.append(left_index)
        left_index >>= 1

    return propagate_node_indexes

def update_range_assignment(update_left, update_right, value_to_set):

    left_position = update_left + segment_tree_element_count
    right_position = update_right + segment_tree_element_count

    left_position //= (left_position & (-left_position))
    right_position //= (right_position & (-right_position))

    nodes_to_propagate = get_propagate_indexes(left_position, right_position)

    for node_index in reversed(nodes_to_propagate):
        if segment_tree_lazy[node_index] is not None:
            assign_value = segment_tree_lazy[node_index] * \
                (1 << (segment_tree_height - 1 - node_index.bit_length()))
            segment_tree_lazy[node_index << 1] = segment_tree_lazy[1 + (node_index << 1)] = segment_tree_lazy[node_index]
            segment_tree_nodes[node_index << 1] = segment_tree_nodes[1 + (node_index << 1)] = assign_value
            segment_tree_lazy[node_index] = None

    while left_position != right_position:
        if left_position > right_position:
            segment_tree_nodes[left_position] = value_to_set * (1 << (segment_tree_height - left_position.bit_length()))
            segment_tree_lazy[left_position] = value_to_set
            left_position += 1
            left_position //= (left_position & (-left_position))
        else:
            right_position -= 1
            segment_tree_nodes[right_position] = value_to_set * (1 << (segment_tree_height - right_position.bit_length()))
            segment_tree_lazy[right_position] = value_to_set
            right_position //= (right_position & (-right_position))

    for node_index in nodes_to_propagate:
        segment_tree_nodes[node_index] = segment_tree_nodes[node_index << 1] + segment_tree_nodes[1 + (node_index << 1)]

def range_sum_query(query_left, query_right):

    left_position = query_left + segment_tree_element_count
    right_position = query_right + segment_tree_element_count

    left_position //= (left_position & (-left_position))
    right_position //= (right_position & (-right_position))

    nodes_to_propagate = get_propagate_indexes(left_position, right_position)

    for node_index in reversed(nodes_to_propagate):
        if segment_tree_lazy[node_index] is not None:
            assign_value = segment_tree_lazy[node_index] * \
                (1 << (segment_tree_height - 1 - node_index.bit_length()))
            segment_tree_lazy[node_index << 1] = segment_tree_lazy[1 + (node_index << 1)] = segment_tree_lazy[node_index]
            segment_tree_nodes[node_index << 1] = segment_tree_nodes[1 + (node_index << 1)] = assign_value
            segment_tree_lazy[node_index] = None

    total_sum = 0

    while left_position != right_position:
        if left_position > right_position:
            total_sum += segment_tree_nodes[left_position]
            left_position += 1
            left_position //= (left_position & (-left_position))
        else:
            right_position -= 1
            total_sum += segment_tree_nodes[right_position]
            right_position //= (right_position & (-right_position))

    return total_sum

answers_to_queries = []

for _ in range(number_of_queries):
    query_parameters = list(map(int, read_input_line().split()))
    operation_type = query_parameters[0]

    if operation_type == 0:
        left_update_index = query_parameters[1]
        right_update_index = query_parameters[2]
        value_assignment = query_parameters[3]

        update_range_assignment(left_update_index, right_update_index + 1, value_assignment)
    else:
        left_query_index = query_parameters[1]
        right_query_index = query_parameters[2]

        result = range_sum_query(left_query_index, right_query_index + 1)
        answers_to_queries.append(result)

for result in answers_to_queries:
    print(result)