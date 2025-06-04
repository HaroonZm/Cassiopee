import sys

read_next_line_from_stdin = sys.stdin.readline

number_of_elements, number_of_queries = map(int, read_next_line_from_stdin().split())

maximum_bit_length_needed = (number_of_elements - 1).bit_length()
segment_tree_capacity = 2 ** maximum_bit_length_needed

segment_tree_values = [0] * (2 * segment_tree_capacity)
segment_tree_lazy_values = [None] * (2 * segment_tree_capacity)

segment_tree_height_table = [None]
for height_index in range(maximum_bit_length_needed + 1):
    power_of_two = 2 ** (maximum_bit_length_needed - height_index)
    segment_tree_height_table += [power_of_two] * (2 ** height_index)

def get_affected_tree_indices(start_index_exclusive, end_index_exclusive):
    left_parent = (start_index_exclusive + segment_tree_capacity) >> 1
    right_parent = (end_index_exclusive + segment_tree_capacity) >> 1

    left_bit_length = 0 if start_index_exclusive & 1 else (left_parent & -left_parent).bit_length()
    right_bit_length = 0 if end_index_exclusive & 1 else (right_parent & -right_parent).bit_length()

    for current_level in range(maximum_bit_length_needed):
        if right_bit_length <= current_level:
            yield right_parent
        if left_parent < right_parent and left_bit_length <= current_level:
            yield left_parent
        left_parent >>= 1
        right_parent >>= 1

def propagate_pending_lazy_updates(nodes_to_propagate):
    for node_index in reversed(nodes_to_propagate):
        pending_value = segment_tree_lazy_values[node_index]
        if pending_value is None:
            continue
        segment_tree_lazy_values[2 * node_index] = pending_value // 2
        segment_tree_values[2 * node_index] = pending_value // 2
        segment_tree_lazy_values[2 * node_index + 1] = pending_value // 2
        segment_tree_values[2 * node_index + 1] = pending_value // 2
        segment_tree_lazy_values[node_index] = None

def assign_value_on_range(start_index, end_index_non_inclusive, value_to_assign):
    affected_tree_indices = list(get_affected_tree_indices(start_index, end_index_non_inclusive))
    propagate_pending_lazy_updates(affected_tree_indices)

    left = segment_tree_capacity + start_index
    right = segment_tree_capacity + end_index_non_inclusive

    while left < right:
        if right & 1:
            right -= 1
            segment_tree_lazy_values[right] = value_to_assign * segment_tree_height_table[right]
            segment_tree_values[right] = value_to_assign * segment_tree_height_table[right]
        if left & 1:
            segment_tree_lazy_values[left] = value_to_assign * segment_tree_height_table[left]
            segment_tree_values[left] = value_to_assign * segment_tree_height_table[left]
            left += 1
        left >>= 1
        right >>= 1

    for node_index in affected_tree_indices:
        if 2 * node_index + 1 < segment_tree_capacity * 2:
            segment_tree_values[node_index] = segment_tree_values[2 * node_index] + segment_tree_values[2 * node_index + 1]

def query_range_sum(start_index, end_index_non_inclusive):
    affected_tree_indices = list(get_affected_tree_indices(start_index, end_index_non_inclusive))
    propagate_pending_lazy_updates(affected_tree_indices)

    left = segment_tree_capacity + start_index
    right = segment_tree_capacity + end_index_non_inclusive

    summation_result = 0
    while left < right:
        if right & 1:
            right -= 1
            summation_result += segment_tree_values[right]
        if left & 1:
            summation_result += segment_tree_values[left]
            left += 1
        left >>= 1
        right >>= 1
    return summation_result

query_results = []
for current_query_index in range(number_of_queries):
    command_and_parameters = list(map(int, read_next_line_from_stdin().split()))
    command_type, *optional_query_parameters = command_and_parameters

    if command_type:
        left_bound = optional_query_parameters[0]
        right_bound = optional_query_parameters[1] + 1
        query_result = query_range_sum(left_bound, right_bound)
        query_results.append(query_result)
    else:
        left_bound = optional_query_parameters[0]
        right_bound = optional_query_parameters[1] + 1
        assignment_value = optional_query_parameters[2]
        assign_value_on_range(left_bound, right_bound, assignment_value)

print('\n'.join(map(str, query_results)))