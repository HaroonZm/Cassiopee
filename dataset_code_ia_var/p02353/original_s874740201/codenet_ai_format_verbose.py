#!/usr/bin/env python3
import sys

# Increase recursion limit for deep recursion
sys.setrecursionlimit(10 ** 6)

# Read input efficiently
input = sys.stdin.buffer.readline

# Constants for infinity and modulo
INFINITY_LIMIT = 10 ** 9 + 1
MODULO_NUMBER = 10 ** 9 + 7

def debug_output(*debug_values):
    print(*debug_values, file=sys.stderr)

def set_segment_tree_depth(segment_tree_depth):
    global SEGMENT_TREE_DEPTH, SEGMENT_TREE_TOTAL_SIZE, SEGMENT_TREE_NON_LEAF_SIZE
    SEGMENT_TREE_DEPTH = segment_tree_depth
    SEGMENT_TREE_TOTAL_SIZE = 1 << SEGMENT_TREE_DEPTH
    SEGMENT_TREE_NON_LEAF_SIZE = 1 << (SEGMENT_TREE_DEPTH - 1)

def set_segment_tree_width(number_of_elements):
    set_segment_tree_depth((number_of_elements - 1).bit_length() + 1)

def get_node_leaf_size(node_position):
    position_bit_length = node_position.bit_length()
    return (1 << (SEGMENT_TREE_DEPTH - position_bit_length))

def lift_node_to_root(node_position):
    node_position += SEGMENT_TREE_TOTAL_SIZE // 2
    return node_position // (node_position & -node_position)

def propagate_up_tree(segment_tree_values, node_position, binary_operation):
    while node_position > 1:
        node_position >>= 1
        segment_tree_values[node_position] = binary_operation(
            segment_tree_values[node_position * 2],
            segment_tree_values[node_position * 2 + 1]
        )

def propagate_forced_down(
    lazy_action_table, segment_tree_values, node_position,
    action_composite_function, action_force_function, action_unity_value
):
    node_level = node_position.bit_length() - 1
    subtree_size = SEGMENT_TREE_NON_LEAF_SIZE
    for current_level in range(node_level):
        subtree_size //= 2
        tree_index = node_position >> (node_level - current_level)
        current_action = lazy_action_table[tree_index]
        if current_action != action_unity_value:
            lazy_action_table[tree_index * 2] = current_action
            lazy_action_table[tree_index * 2 + 1] = current_action
            lazy_action_table[tree_index] = action_unity_value
            segment_tree_values[tree_index * 2] = current_action * subtree_size
            segment_tree_values[tree_index * 2 + 1] = current_action * subtree_size

def force_update_range(
    segment_tree_values, lazy_action_table, left_index, right_index,
    update_action, action_force_function, action_composite_function, action_unity_value
):
    """
    - action_force_function: (action, value, cell_size) => new_value
    - action_composite_function: (new_action, old_action) => composite_action
    """
    left_index += SEGMENT_TREE_NON_LEAF_SIZE
    right_index += SEGMENT_TREE_NON_LEAF_SIZE
    while left_index < right_index:
        if left_index & 1:
            segment_tree_values[left_index] = action_force_function(
                update_action, segment_tree_values[left_index], get_node_leaf_size(left_index)
            )
            lazy_action_table[left_index] = action_composite_function(update_action, lazy_action_table[left_index])
            left_index += 1
        if right_index & 1:
            right_index -= 1
            segment_tree_values[right_index] = action_force_function(
                update_action, segment_tree_values[right_index], get_node_leaf_size(right_index)
            )
            lazy_action_table[right_index] = action_composite_function(update_action, lazy_action_table[right_index])
        left_index //= 2
        right_index //= 2

def reduce_range(
    segment_tree_values, left_index, right_index,
    binary_operation, unity_value
):
    result_from_left = unity_value
    result_from_right = unity_value
    left_index += SEGMENT_TREE_NON_LEAF_SIZE
    right_index += SEGMENT_TREE_NON_LEAF_SIZE
    while left_index < right_index:
        if left_index & 1:
            result_from_left = binary_operation(result_from_left, segment_tree_values[left_index])
            left_index += 1
        if right_index & 1:
            right_index -= 1
            result_from_right = binary_operation(segment_tree_values[right_index], result_from_right)
        left_index //= 2
        right_index //= 2
    return binary_operation(result_from_left, result_from_right)

def perform_lazy_range_update(
    lazy_action_table, segment_tree_values, update_start, update_end,
    update_action, action_composite_function, action_force_function, action_unity_value, value_binary_operation
):
    """
    Perform a lazy update over [update_start, update_end)
    """
    propagated_left = lift_node_to_root(update_start)
    propagated_right = lift_node_to_root(update_end)
    propagate_forced_down(
        lazy_action_table, segment_tree_values, propagated_left,
        action_composite_function, action_force_function, action_unity_value
    )
    propagate_forced_down(
        lazy_action_table, segment_tree_values, propagated_right,
        action_composite_function, action_force_function, action_unity_value
    )
    force_update_range(
        segment_tree_values, lazy_action_table, update_start, update_end,
        update_action, action_force_function, action_composite_function, action_unity_value
    )
    propagate_up_tree(segment_tree_values, propagated_left, value_binary_operation)
    propagate_up_tree(segment_tree_values, propagated_right, value_binary_operation)

def perform_lazy_range_query(
    lazy_action_table, segment_tree_values, query_start, query_end,
    action_composite_function, action_force_function, action_unity_value,
    value_binary_operation, value_unity_element
):
    """
    Query/reduce over [query_start, query_end)
    """
    propagate_forced_down(
        lazy_action_table, segment_tree_values, lift_node_to_root(query_start),
        action_composite_function, action_force_function, action_unity_value
    )
    propagate_forced_down(
        lazy_action_table, segment_tree_values, lift_node_to_root(query_end),
        action_composite_function, action_force_function, action_unity_value
    )
    return reduce_range(
        segment_tree_values, query_start, query_end, value_binary_operation, value_unity_element
    )

def print_segment_tree_debug(
    segment_tree_values,
    minimum_string_size=0,
    maximum_string_size_limit=None
):
    global SEGMENT_TREE_DEPTH
    value_strings = [str(x) for x in segment_tree_values]
    if maximum_string_size_limit is not None:
        for i in range(SEGMENT_TREE_NON_LEAF_SIZE, SEGMENT_TREE_TOTAL_SIZE):
            value_strings[i] = value_strings[i][:maximum_string_size_limit]
    formatted_string_length = max(len(s) for s in value_strings[SEGMENT_TREE_NON_LEAF_SIZE:])
    if formatted_string_length > minimum_string_size:
        minimum_string_size = formatted_string_length

    tree_levels_debug_lines = ["|"] * SEGMENT_TREE_DEPTH
    current_level = 0
    next_level_index = 2
    for index in range(1, SEGMENT_TREE_TOTAL_SIZE):
        if index == next_level_index:
            current_level += 1
            next_level_index *= 2
        subtree_width = ((minimum_string_size + 1) << (SEGMENT_TREE_DEPTH - 1 - current_level)) - 1
        tree_levels_debug_lines[current_level] += value_strings[index].center(subtree_width) + "|"
    print(*tree_levels_debug_lines, sep="\n", file=sys.stderr)

def main():
    from operator import add as operator_addition
    number_of_elements, number_of_queries = map(int, input().split())
    set_segment_tree_width(number_of_elements)

    segment_tree_value_unity = 0
    segment_tree_values = [0] * SEGMENT_TREE_TOTAL_SIZE
    value_binary_operation = operator_addition
    lazy_action_unity_value = None
    lazy_action_table = [lazy_action_unity_value] * SEGMENT_TREE_TOTAL_SIZE

    def force_update_function(current_action, present_value, value_size):
        if current_action == lazy_action_unity_value:
            return present_value
        return current_action * value_size

    def composite_action_function(new_action, existing_action):
        if new_action != lazy_action_unity_value:
            return new_action
        return existing_action

    for _ in range(number_of_queries):
        query_info = list(map(int, input().split()))
        query_type, *query_arguments = query_info
        if query_type == 0:
            # Run update operation
            range_start, range_end, update_value = query_arguments
            perform_lazy_range_update(
                lazy_action_table, segment_tree_values, range_start, range_end + 1,
                update_value, composite_action_function, force_update_function, lazy_action_unity_value, value_binary_operation
            )
        else:
            # Run get-sum operation
            query_start, query_end = query_arguments
            print(
                perform_lazy_range_query(
                    lazy_action_table, segment_tree_values, query_start, query_end + 1,
                    composite_action_function, force_update_function, lazy_action_unity_value, value_binary_operation, segment_tree_value_unity
                )
            )

# Test string input (for testing, not production)
TEST_INPUT_SAMPLE = """
6 7
0 1 3 1
0 2 4 -2
1 0 5
1 0 1
0 3 5 3
1 3 4
1 0 5
"""

TEST_PROCEDURE_SAMPLE = """
>>> as_input(TEST_INPUT_SAMPLE)
>>> main()
-5
1
6
8
"""

def _run_doctest():
    import doctest
    doctest.testmod()
    global_variables = globals()
    for variable_name in sorted(global_variables):
        if variable_name.startswith("TEST_"):
            doctest.run_docstring_examples(global_variables[variable_name], global_variables)

def as_input(input_string):
    """
    Use in test: feed the provided string as system input.
    """
    import io
    global read, input
    string_io_object = io.StringIO(input_string.strip())
    def input():
        return bytes(string_io_object.readline(), "ascii")
    def read():
        return bytes(string_io_object.read(), "ascii")
input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

if sys.argv[-1] == "-t":
    print("testing")
    _run_doctest()
    sys.exit()

main()