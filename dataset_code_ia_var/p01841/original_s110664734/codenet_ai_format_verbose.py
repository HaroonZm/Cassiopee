def find_bracket_indices(start_index, end_index, sequence):

    open_parentheses_count = 0
    left_bracket_index = 0
    right_bracket_index = 0

    for current_index in range(start_index, end_index + 1):

        if sequence[current_index] == '(':
            open_parentheses_count += 1

        elif sequence[current_index] == ')':
            open_parentheses_count -= 1

        elif open_parentheses_count == 0 and sequence[current_index] == "[":
            left_bracket_index = current_index

        elif open_parentheses_count == 0 and sequence[current_index] == "]":
            right_bracket_index = current_index

    return left_bracket_index, right_bracket_index




def recursive_parser(
    string1_start,
    string1_end,
    string2_start,
    string2_end
):

    global input_string1
    global input_string2

    node1_left_index, node1_right_index = find_bracket_indices(
        string1_start,
        string1_end,
        input_string1
    )

    node2_left_index, node2_right_index = find_bracket_indices(
        string2_start,
        string2_end,
        input_string2
    )

    node_value_sum = int(
        input_string1[node1_left_index + 1 : node1_right_index]
    ) + int(
        input_string2[node2_left_index + 1 : node2_right_index]
    )

    node_string = "[{}]".format(node_value_sum)

    if min(
        node1_left_index - string1_start,
        node2_left_index - string2_start
    ) <= 2:

        left_subtree = "()"

    else:

        left_subtree = "({})".format(
            recursive_parser(
                string1_start + 1,
                node1_left_index - 2,
                string2_start + 1,
                node2_left_index - 2
            )
        )

    if min(
        string1_end - node1_right_index,
        string2_end - node2_right_index
    ) <= 2:

        right_subtree = "()"

    else:

        right_subtree = "({})".format(
            recursive_parser(
                node1_right_index + 2,
                string1_end - 1,
                node2_right_index + 2,
                string2_end - 1
            )
        )

    return left_subtree + node_string + right_subtree




input_string1 = input()
input_string2 = input()

print(
    recursive_parser(
        0,
        len(input_string1) - 1,
        0,
        len(input_string2) - 1
    )
)