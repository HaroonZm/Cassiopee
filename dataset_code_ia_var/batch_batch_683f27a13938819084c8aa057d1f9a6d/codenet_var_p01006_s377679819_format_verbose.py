mapping_reference = {
    "A": "BD",
    "B": "ACE",
    "C": "BF",
    "D": "AEG",
    "E": "BDFH",
    "F": "CEI",
    "G": "DH",
    "H": "EGI",
    "I": "HF"
}

number_of_inputs_to_process = 1000

for input_counter in range(number_of_inputs_to_process):

    user_input_sequence = raw_input()

    for current_index in range(len(user_input_sequence) - 1):

        current_character = user_input_sequence[current_index]
        next_character = user_input_sequence[current_index + 1]

        allowed_next_characters = mapping_reference[current_character]

        if next_character not in allowed_next_characters:
            break

    else:
        print user_input_sequence