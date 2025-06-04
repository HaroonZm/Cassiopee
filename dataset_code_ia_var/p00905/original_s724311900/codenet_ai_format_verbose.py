import re

while True:

    possible_indent_weights_round = []
    possible_indent_weights_curly = []
    possible_indent_weights_square = []

    number_of_reference_lines, number_of_query_lines = map(int, input().split())
    if number_of_reference_lines == 0 and number_of_query_lines == 0:
        break

    leading_dot_counts_per_line = []
    cumulative_parentheses_balance = [0]
    cumulative_curly_braces_balance = [0]
    cumulative_square_brackets_balance = [0]

    for _ in range(number_of_reference_lines):
        code_line = input()
        count_character = code_line.count

        leading_dot_count = re.match(r'[.]*', code_line).span()[1]
        leading_dot_counts_per_line.append(leading_dot_count)

        cumulative_parentheses_balance.append(cumulative_parentheses_balance[-1] + count_character('(') - count_character(')'))
        cumulative_curly_braces_balance.append(cumulative_curly_braces_balance[-1] + count_character('{') - count_character('}'))
        cumulative_square_brackets_balance.append(cumulative_square_brackets_balance[-1] + count_character('[') - count_character(']'))

    for possible_weight_round in range(1, 21):
        for possible_weight_curly in range(1, 21):
            for possible_weight_square in range(1, 21):

                for (
                    expected_dot_count,
                    open_parentheses_count,
                    open_curly_braces_count,
                    open_square_brackets_count
                ) in zip(
                    leading_dot_counts_per_line,
                    cumulative_parentheses_balance,
                    cumulative_curly_braces_balance,
                    cumulative_square_brackets_balance
                ):
                    calculated_indent = (
                        open_parentheses_count * possible_weight_round +
                        open_curly_braces_count * possible_weight_curly +
                        open_square_brackets_count * possible_weight_square
                    )
                    if calculated_indent != expected_dot_count:
                        break
                else:
                    possible_indent_weights_round.append(possible_weight_round)
                    possible_indent_weights_curly.append(possible_weight_curly)
                    possible_indent_weights_square.append(possible_weight_square)

    query_cumulative_parentheses_balance = [0]
    query_cumulative_curly_braces_balance = [0]
    query_cumulative_square_brackets_balance = [0]

    for _ in range(number_of_query_lines):
        code_line = input()
        count_character = code_line.count

        query_cumulative_parentheses_balance.append(
            query_cumulative_parentheses_balance[-1] + count_character('(') - count_character(')')
        )
        query_cumulative_curly_braces_balance.append(
            query_cumulative_curly_braces_balance[-1] + count_character('{') - count_character('}')
        )
        query_cumulative_square_brackets_balance.append(
            query_cumulative_square_brackets_balance[-1] + count_character('[') - count_character(']')
        )

    query_cumulative_parentheses_balance = query_cumulative_parentheses_balance[:-1]
    query_cumulative_curly_braces_balance = query_cumulative_curly_braces_balance[:-1]
    query_cumulative_square_brackets_balance = query_cumulative_square_brackets_balance[:-1]

    possible_query_line_indents = [set() for _ in range(number_of_query_lines)]

    for (
        possible_weight_round,
        possible_weight_curly,
        possible_weight_square
    ) in zip(
        possible_indent_weights_round,
        possible_indent_weights_curly,
        possible_indent_weights_square
    ):
        for line_index, (
            query_open_parentheses_count,
            query_open_curly_braces_count,
            query_open_square_brackets_count
        ) in enumerate(
            zip(
                query_cumulative_parentheses_balance,
                query_cumulative_curly_braces_balance,
                query_cumulative_square_brackets_balance
            )
        ):
            calculated_query_indent = (
                query_open_parentheses_count * possible_weight_round +
                query_open_curly_braces_count * possible_weight_curly +
                query_open_square_brackets_count * possible_weight_square
            )
            possible_query_line_indents[line_index].add(calculated_query_indent)

    result_indentations_per_query_line = [
        list(possible_indents)[0] if len(possible_indents) == 1 else -1
        for possible_indents in possible_query_line_indents
    ]

    print(*result_indentations_per_query_line)