user_input_string = input()

number_of_adjacent_different_characters = 0

for character_index in range(1, len(user_input_string)):

    if user_input_string[character_index] != user_input_string[character_index - 1]:

        number_of_adjacent_different_characters += 1

print(number_of_adjacent_different_characters)