class BinaryTree:
    def __init__(self, node_value, left_subtree=None, right_subtree=None):
        self.node_value = node_value
        self.left_subtree = left_subtree
        self.right_subtree = right_subtree


def find_corresponding_bracket(string, bracket_open, bracket_close):
    current_depth = 0
    corresponding_index = -1

    for current_index in range(len(string)):
        if string[current_index] == bracket_open:
            current_depth += 1
        elif string[current_index] == bracket_close:
            if current_depth == 1:
                corresponding_index = current_index
                break
            else:
                current_depth -= 1

    return corresponding_index


def build_binary_tree_from_string(tree_string):
    if tree_string == '':
        return None

    left_start_index = 0
    left_end_index = find_corresponding_bracket(tree_string, '(', ')') + 1
    value_start_index = left_end_index
    value_end_index = value_start_index + find_corresponding_bracket(tree_string[value_start_index:], '[', ']') + 1
    right_start_index = value_end_index + 1
    right_end_index = len(tree_string) - 1

    node_value = int(tree_string[value_start_index + 1: value_end_index - 1])
    left_subtree = build_binary_tree_from_string(tree_string[left_start_index + 1: left_end_index - 1])
    right_subtree = build_binary_tree_from_string(tree_string[right_start_index: right_end_index])

    binary_tree_node = BinaryTree(node_value, left_subtree, right_subtree)
    return binary_tree_node


def synthesize_trees(tree_first, tree_second):
    synthesized_tree = BinaryTree(node_value=tree_first.node_value + tree_second.node_value)

    if tree_first.left_subtree is not None and tree_second.left_subtree is not None:
        synthesized_tree.left_subtree = synthesize_trees(tree_first.left_subtree, tree_second.left_subtree)

    if tree_first.right_subtree is not None and tree_second.right_subtree is not None:
        synthesized_tree.right_subtree = synthesize_trees(tree_first.right_subtree, tree_second.right_subtree)

    return synthesized_tree


def binary_tree_to_string(tree_root):
    if tree_root is None:
        return ''

    left_subtree_string = '(' + binary_tree_to_string(tree_root.left_subtree) + ')'
    node_value_string = '[' + str(tree_root.node_value) + ']'
    right_subtree_string = '(' + binary_tree_to_string(tree_root.right_subtree) + ')'

    return left_subtree_string + node_value_string + right_subtree_string


first_tree_string = input()
second_tree_string = input()

first_tree_root = build_binary_tree_from_string(first_tree_string)
second_tree_root = build_binary_tree_from_string(second_tree_string)

synthesized_root = synthesize_trees(first_tree_root, second_tree_root)

print(binary_tree_to_string(synthesized_root))