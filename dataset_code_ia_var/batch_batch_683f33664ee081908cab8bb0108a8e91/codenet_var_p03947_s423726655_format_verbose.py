user_input_string = str(input())

number_of_character_changes = 0

for character_index in range(len(user_input_string) - 1):

    if user_input_string[character_index + 1] != user_input_string[character_index]:

        number_of_character_changes += 1

print(number_of_character_changes)