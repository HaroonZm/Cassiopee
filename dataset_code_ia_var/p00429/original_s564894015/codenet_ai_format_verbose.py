def look_and_say_sequence(initial_sequence, number_of_iterations):

    for iteration_index in range(number_of_iterations):

        next_sequence = ""
        current_character = initial_sequence[0]
        current_character_count = 1

        for character_index in range(1, len(initial_sequence)):

            if initial_sequence[character_index] == current_character:
                current_character_count += 1
            else:
                next_sequence += str(current_character_count) + current_character
                current_character = initial_sequence[character_index]
                current_character_count = 1

        initial_sequence = next_sequence + str(current_character_count) + current_character

    return initial_sequence


while True:

    number_of_iterations = input()
    if number_of_iterations == 0:
        break

    input_sequence = raw_input()
    print look_and_say_sequence(input_sequence, number_of_iterations)