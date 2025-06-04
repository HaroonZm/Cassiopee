user_input_string = raw_input()

input_character_list = list(user_input_string)

previous_character = input_character_list[0]

number_of_character_changes = 0

for current_character in input_character_list:
    if current_character != previous_character:
        number_of_character_changes += 1
        previous_character = current_character

print number_of_character_changes