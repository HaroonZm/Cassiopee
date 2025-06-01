from collections import deque

def replace_pair_with_color(input_string, index, replacement_color):
    return input_string[:index] + replacement_color * 2 + input_string[index + 2:]

def process_color_string(input_string):
    string_length = len(input_string)
    monotone_colors = ["r" * string_length, "g" * string_length, "b" * string_length]
    if input_string in monotone_colors:
        print(0)
        return

    color_pairs_to_third = {
        ("r", "g"): "b", ("g", "r"): "b",
        ("r", "b"): "g", ("b", "r"): "g",
        ("g", "b"): "r", ("b", "g"): "r"
    }
    visited_strings = {input_string: 0}
    queue = deque()
    queue_append = queue.append
    queue_pop_left = queue.popleft
    queue_append((input_string, 0))

    while queue:
        current_string, current_steps = queue_pop_left()
        next_steps = current_steps + 1
        prev_char = current_string[0]

        for pos in range(1, string_length):
            current_char = current_string[pos]
            if current_char != prev_char:
                new_string = replace_pair_with_color(current_string, pos - 1, color_pairs_to_third[(current_char, prev_char)])

                if new_string in monotone_colors:
                    print(next_steps)
                    return

                if new_string not in visited_strings:
                    visited_strings[new_string] = next_steps
                    queue_append((new_string, next_steps))

            prev_char = current_char

    print("NA")

def main():
    while True:
        user_input = input()
        if user_input == "0":
            break
        process_color_string(user_input)

main()