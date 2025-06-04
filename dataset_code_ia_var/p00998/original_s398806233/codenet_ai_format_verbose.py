VERY_LARGE_NUMBER = 10**9

def update_node_minimum(node):
    if node:
        left_child = node[0]
        right_child = node[1]
        node[4] = min(
            (left_child[4] if left_child else VERY_LARGE_NUMBER),
            (right_child[4] if right_child else VERY_LARGE_NUMBER),
            node[2]
        )

def splay_node(parent_stack, direction_stack, target_node):
    left_child = target_node[0]
    right_child = target_node[1]
    left_size = (left_child[3] if left_child else 0)
    right_size = (right_child[3] if right_child else 0)
    loop_count = len(parent_stack) >> 1

    while loop_count:
        current_node = parent_stack.pop()
        grandparent_node = parent_stack.pop()
        current_direction = direction_stack.pop()
        parent_direction = direction_stack.pop()

        if current_direction == parent_direction:
            grandparent_node[3] = size_delta = grandparent_node[3] - left_size - right_size - 2
            if current_direction:
                grandparent_node[1] = current_node[0]
                current_node[0] = grandparent_node
                current_node[1] = left_child
                left_child = current_node
                left_child[3] = left_size = size_delta + left_size + 1
            else:
                grandparent_node[0] = current_node[1]
                current_node[1] = grandparent_node
                current_node[0] = right_child
                right_child = current_node
                right_child[3] = right_size = size_delta + right_size + 1
        else:
            if current_direction:
                current_node[1] = left_child
                left_child = current_node
                grandparent_node[0] = right_child
                right_child = grandparent_node
                left_child[3] = left_size = left_child[3] - right_size - 1
                right_child[3] = right_size = right_child[3] - left_size - 1
            else:
                current_node[0] = right_child
                right_child = current_node
                grandparent_node[1] = left_child
                left_child = grandparent_node
                right_child[3] = right_size = right_child[3] - left_size - 1
                left_child[3] = left_size = left_child[3] - right_size - 1
        loop_count -= 1
        update_node_minimum(grandparent_node)
        update_node_minimum(current_node)

    if parent_stack:
        last_node = parent_stack[0]
        last_direction = direction_stack[0]
        if last_direction:
            last_node[1] = left_child
            left_child = last_node
            left_child[3] = left_size = left_child[3] - right_size - 1
        else:
            last_node[0] = right_child
            right_child = last_node
            right_child[3] = right_size = right_child[3] - left_size - 1
        update_node_minimum(last_node)

    target_node[0] = left_child
    target_node[1] = right_child
    target_node[3] = left_size + right_size + 1
    update_node_minimum(target_node)
    return target_node

def create_new_node(node_value):
    return [None, None, node_value, 1, node_value]

def merge_trees(left_tree, right_tree):
    if not left_tree or not right_tree:
        return left_tree or right_tree
    if not left_tree[1]:
        left_tree[3] += right_tree[3]
        left_tree[1] = right_tree
        return left_tree

    parent_stack = []
    rightmost_node = left_tree
    while rightmost_node[1]:
        parent_stack.append(rightmost_node)
        rightmost_node = rightmost_node[1]

    left_tree = splay_node(parent_stack, [1]*len(parent_stack), rightmost_node)
    left_tree[3] += right_tree[3]
    left_tree[1] = right_tree
    update_node_minimum(left_tree)
    return left_tree

def split_tree_at_position(input_tree, split_index):
    if not input_tree:
        return None, None
    if not 0 < split_index < input_tree[3]:
        if split_index == input_tree[3]:
            return find_kth_element(input_tree, split_index), None
        return None, input_tree

    current_node = input_tree
    parent_stack = []
    direction_stack = []

    while current_node:
        left_child = current_node[0]
        rank = (left_child[3] if left_child else 0) + 1
        if rank == split_index:
            break
        parent_stack.append(current_node)
        if rank < split_index:
            split_index -= rank
            current_node = current_node[1]
            direction_stack.append(1)
        else:
            current_node = current_node[0]
            direction_stack.append(0)

    left_tree = splay_node(parent_stack, direction_stack, current_node)
    right_tree = left_tree[1]
    if right_tree:
        left_tree[3] -= right_tree[3]
    left_tree[1] = None
    update_node_minimum(left_tree)
    return left_tree, right_tree

def find_kth_element(tree_root, kth_index):
    if not tree_root or not 0 < kth_index <= tree_root[3]:
        return tree_root
    current_node = tree_root
    parent_stack = []
    direction_stack = []
    while current_node:
        left_child = current_node[0]
        rank = (left_child[3] if left_child else 0) + 1
        if rank == kth_index:
            break
        parent_stack.append(current_node)
        if rank < kth_index:
            kth_index -= rank
            current_node = current_node[1]
            direction_stack.append(1)
        else:
            current_node = current_node[0]
            direction_stack.append(0)
    return splay_node(parent_stack, direction_stack, current_node)

def print_debug_tree(root_node):
    def depth_first_search(node, indentation_level):
        if node[0]:
            depth_first_search(node[0], indentation_level + 1)
        print(" " * indentation_level, node[2:])
        if node[1]:
            depth_first_search(node[1], indentation_level + 1)
    depth_first_search(root_node, 0)

read_line_from_input = open(0).readline
write_lines_to_output = open(1, 'w').writelines

number_of_elements, number_of_queries = map(int, read_line_from_input().split())
splay_tree_root = previous_node = create_new_node(int(read_line_from_input()))
previous_node[3] = number_of_elements
for position_in_sequence in range(number_of_elements - 1):
    previous_node[1] = previous_node = create_new_node(int(read_line_from_input()))
    previous_node[3] = number_of_elements - 1 - position_in_sequence

answer_lines = []
for query_index in range(number_of_queries):
    query_type, left_index, right_index = map(int, read_line_from_input().split())
    if query_type == 0:
        left_split, right_split = split_tree_at_position(splay_tree_root, right_index + 1)
        target_node = left_split
        left_split = left_split[0]
        middle_split, left_split = split_tree_at_position(left_split, left_index)
        merged_right = merge_trees(left_split, right_split)
        target_node[0] = middle_split
        target_node[3] = (middle_split[3] if middle_split else 0) + 1
        update_node_minimum(target_node)
        splay_tree_root = merge_trees(target_node, merged_right)
    elif query_type == 1:
        left_split, right_split = split_tree_at_position(splay_tree_root, right_index + 1)
        middle_split, left_split = split_tree_at_position(left_split, left_index)
        answer_lines.append("%d\n" % left_split[4])
        merged_right = merge_trees(left_split, right_split)
        splay_tree_root = merge_trees(middle_split, merged_right)
    else:
        splay_tree_root = find_kth_element(splay_tree_root, left_index + 1)
        splay_tree_root[2] = right_index
        update_node_minimum(splay_tree_root)

write_lines_to_output(answer_lines)