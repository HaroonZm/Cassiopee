from collections import deque

def replace_substring_with_color(input_string, start_index, replacement_color):
    return input_string[:start_index] + replacement_color * 2 + input_string[start_index + 2:]

def find_minimum_operations_to_monochrome(initial_color_string):
    string_length = len(initial_color_string)
    monochrome_variants = ["r" * string_length, "g" * string_length, "b" * string_length]

    if initial_color_string in monochrome_variants:
        print(0)
        return

    possible_colors = "rgb"
    color_combination_to_result = {
        ("r", "g"): "b", ("g", "r"): "b",
        ("r", "b"): "g", ("b", "r"): "g",
        ("g", "b"): "r", ("b", "g"): "r"
    }

    already_visited_states = {initial_color_string: 0}

    queue_states_and_steps = deque()
    queue_states_and_steps.append((initial_color_string, 0))

    while queue_states_and_steps:
        current_colors, current_step_count = queue_states_and_steps.popleft()
        next_step_count = current_step_count + 1
        previous_color = current_colors[0]

        for index in range(1, string_length):
            current_color = current_colors[index]
            if current_color != previous_color:
                generated_new_string = replace_substring_with_color(
                    current_colors,
                    index - 1,
                    color_combination_to_result[(current_color, previous_color)]
                )

                if generated_new_string in monochrome_variants:
                    print(next_step_count)
                    return

                if generated_new_string not in already_visited_states:
                    already_visited_states[generated_new_string] = next_step_count
                    queue_states_and_steps.append((generated_new_string, next_step_count))

            previous_color = current_color

    print("NA")

def execute_until_zero_input():
    while True:
        color_input_string = input()
        if color_input_string == "0":
            break
        find_minimum_operations_to_monochrome(color_input_string)

execute_until_zero_input()