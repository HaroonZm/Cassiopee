maximum_number_of_inputs = 1000

adjacent_letter_rules = {
    "A": ["B", "D"],
    "B": ["A", "C", "E"],
    "C": ["B", "F"],
    "D": ["A", "E", "G"],
    "E": ["B", "D", "F", "H"],
    "F": ["C", "E", "I"],
    "G": ["D", "H"],
    "H": ["E", "G", "I"],
    "I": ["F", "H"]
}

def is_string_valid_letter_path(input_string):

    if len(input_string) == 1:
        return True

    for current_position in range(len(input_string) - 1):

        current_letter = input_string[current_position]
        next_letter = input_string[current_position + 1]

        if next_letter not in adjacent_letter_rules[current_letter]:
            return False

    return True

for input_index in range(maximum_number_of_inputs):

    user_input_string = input()

    if is_string_valid_letter_path(user_input_string):
        print(user_input_string)