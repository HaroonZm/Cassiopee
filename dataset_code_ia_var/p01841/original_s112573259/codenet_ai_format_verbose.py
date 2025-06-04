def convert(tree_string):

    current_index = 0

    def parse_tree():
        nonlocal current_index

        if tree_string[current_index] == ')':
            return ()

        current_index += 1  # Skip '('

        left_subtree = parse_tree()

        current_index += 2  # Skip ')['

        node_value = 0
        while tree_string[current_index] != ']':
            node_value = 10 * node_value + int(tree_string[current_index])
            current_index += 1

        current_index += 2  # Skip ']('

        right_subtree = parse_tree()

        current_index += 1  # Skip ')'

        return (left_subtree, node_value, right_subtree)

    return parse_tree()


def add_corresponding_nodes(tree_a, tree_b):

    if not tree_a or not tree_b:
        return ()

    left_sum_subtree = add_corresponding_nodes(tree_a[0], tree_b[0])
    node_sum_value = [tree_a[1] + tree_b[1]]
    right_sum_subtree = add_corresponding_nodes(tree_a[2], tree_b[2])

    return (left_sum_subtree, node_sum_value, right_sum_subtree)


input_tree_string_1 = input()
input_tree_string_2 = input()

parsed_tree_1 = convert(input_tree_string_1)
parsed_tree_2 = convert(input_tree_string_2)

summed_tree = add_corresponding_nodes(parsed_tree_1, parsed_tree_2)

summed_tree_string = str(summed_tree).replace(", ", "")[1:-1]

print(summed_tree_string)