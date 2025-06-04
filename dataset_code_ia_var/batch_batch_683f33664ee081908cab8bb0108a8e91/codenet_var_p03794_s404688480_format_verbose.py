import sys

def build_adjacency_list_from_input(input_string):
    adjacency_list = dict()
    number_of_nodes = None

    for input_line in input_string.splitlines():
        if number_of_nodes is None:
            number_of_nodes = int(input_line.strip())
            for node_label in range(1, number_of_nodes + 1):
                adjacency_list[node_label] = set()
            continue

        node_a, node_b = map(int, input_line.split())
        adjacency_list[node_a].add(node_b)
        adjacency_list[node_b].add(node_a)

    return adjacency_list

def find_longest_path_through_tree(adjacency_list, current_node, parent_node=None):
    paths = [
        find_longest_path_through_tree(adjacency_list, neighbor, parent_node=current_node)
        for neighbor in adjacency_list[current_node]
        if neighbor != parent_node
    ]
    longest_subpath = max(paths, key=len, default=())
    return (current_node,) + longest_subpath

def build_structured_tree_from_graph(adjacency_list, current_node, parent_node=None):
    subtree_list = [
        build_structured_tree_from_graph(adjacency_list, neighbor, parent_node=current_node)
        for neighbor in adjacency_list[current_node]
        if neighbor != parent_node
    ]
    return StructuredTuple(subtree_list)

class StructuredTuple(tuple):
    def __new__(cls, subtree_iterable=()):
        instance = super().__new__(cls, subtree_iterable)
        instance.height = (
            1 + min((subtree.height[0] for subtree in instance), default=-1),
            1 + max((subtree.height[1] for subtree in instance), default=-1)
        )
        instance.edges = len(instance) + sum(subtree.edges for subtree in instance)
        return instance

def count_valid_combinations(adjacency_list):
    some_node = next(iter(adjacency_list))
    farthest_path = find_longest_path_through_tree(
        adjacency_list,
        find_longest_path_through_tree(adjacency_list, some_node)[-1]
    )
    diameter_length = len(farthest_path)
    diameter_half = diameter_length // 2
    center_root = farthest_path[diameter_length // 2]

    if diameter_length % 2:
        tree_structure = build_structured_tree_from_graph(adjacency_list, center_root)
        total_combinations = 0
        for limit_pair in zip(range(diameter_half + 1), reversed(range(diameter_half + 1))):
            total_combinations += enumerate_limit_combinations(limit_pair, tree_structure)
        return total_combinations
    else:
        left_center = farthest_path[diameter_length // 2 - 1]
        left_subtree = StructuredTuple([build_structured_tree_from_graph(adjacency_list, left_center, parent_node=center_root)])
        right_subtree = build_structured_tree_from_graph(adjacency_list, center_root, parent_node=left_center)

        left_limits_list = [value // 2 for value in range(1, diameter_half * 2 + 2)]
        right_limits_list = [value // 2 for value in range(diameter_half * 2 + 1)]

        left_limit_pairs = list(zip(left_limits_list, reversed(left_limits_list)))
        right_limit_pairs = list(zip(right_limits_list, reversed(right_limits_list)))

        total_combinations = 0
        for limit_index in range(len(left_limit_pairs)):
            current_left_limits = left_limit_pairs[limit_index]
            current_right_limits = right_limit_pairs[limit_index]

            if sum(current_left_limits) > diameter_half:
                left_result = enumerate_limit_combinations(current_left_limits, left_subtree)
                exclude_sums = sum(
                    enumerate_limit_combinations(excluded_limit, left_subtree)
                    for excluded_limit in left_limit_pairs[limit_index - 1 : limit_index] + left_limit_pairs[limit_index + 1 : limit_index + 2]
                )
                left_result -= exclude_sums
            else:
                left_result = enumerate_limit_combinations(current_left_limits, left_subtree)

            right_result = enumerate_limit_combinations(current_right_limits, right_subtree)
            total_combinations += left_result * right_result

        return total_combinations

def enumerate_limit_combinations(limits, tree_shape, memoization_cache=dict()):
    sorted_limits = tuple(sorted(limits))
    row_limit, column_limit = sorted_limits
    min_height, max_height = tree_shape.height

    if row_limit >= max_height:
        return 2 ** tree_shape.edges

    if 0 in sorted_limits:
        return 1

    cache_key = hash((row_limit, column_limit, tree_shape))
    if cache_key not in memoization_cache:
        cumulative_total = 1
        for subtree in tree_shape:
            subtree_accumulator = 0
            for possible_limits in ((row_limit - 1, column_limit), (row_limit, column_limit - 1)):
                subtree_accumulator += enumerate_limit_combinations(possible_limits, subtree)
            cumulative_total *= subtree_accumulator
        memoization_cache[cache_key] = cumulative_total
    return memoization_cache[cache_key]

sys.setrecursionlimit(99999)
adjacency_list = build_adjacency_list_from_input(sys.stdin.read())
result = count_valid_combinations(adjacency_list)
print(result % (10 ** 9 + 7))