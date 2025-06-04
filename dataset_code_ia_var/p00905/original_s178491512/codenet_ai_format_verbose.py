from itertools import product

opening_brackets = "({["
closing_brackets = ")}]"

while True:

    num_sample_lines, num_target_lines = map(int, input().split())

    if num_sample_lines == 0 and num_target_lines == 0:
        break

    sample_code_lines = [input() for _ in range(num_sample_lines)]
    target_code_lines = [input() for _ in range(num_target_lines)]

    possible_indents_per_target_line = [set() for _ in range(num_target_lines)]

    for bracket_weights in product(range(1, 21), repeat=3):

        bracket_depths = [0, 0, 0]  # For (, {, [
        is_valid_weights = True

        for code_line in sample_code_lines:

            first_non_dot_position = 0

            while code_line[first_non_dot_position] == '.':
                first_non_dot_position += 1

            total_indent = sum(depth * weight for depth, weight in zip(bracket_depths, bracket_weights))

            if total_indent != first_non_dot_position:
                is_valid_weights = False
                break

            for character in code_line:
                if character in opening_brackets:
                    bracket_depths[opening_brackets.index(character)] += 1
                elif character in closing_brackets:
                    bracket_depths[closing_brackets.index(character)] -= 1

        if not is_valid_weights:
            continue

        bracket_depths = [0, 0, 0]

        for target_index, target_line in enumerate(target_code_lines):

            first_non_dot_position = 0

            while target_line[first_non_dot_position] == '.':
                first_non_dot_position += 1

            total_indent = sum(depth * weight for depth, weight in zip(bracket_depths, bracket_weights))

            possible_indents_per_target_line[target_index].add(total_indent)

            for character in target_line:
                if character in opening_brackets:
                    bracket_depths[opening_brackets.index(character)] += 1
                elif character in closing_brackets:
                    bracket_depths[closing_brackets.index(character)] -= 1

    indent_results = [0 for _ in range(num_target_lines)]

    for line_index in range(num_target_lines):

        if len(possible_indents_per_target_line[line_index]) > 1:
            indent_results[line_index] = -1
        else:
            (unique_indent_value,) = possible_indents_per_target_line[line_index]
            indent_results[line_index] = unique_indent_value

    print(*indent_results)