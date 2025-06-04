user_input_string = input()

unique_characters_list = list(set(user_input_string))

is_any_character_count_odd = False

for character in unique_characters_list:

    character_count = user_input_string.count(character)

    if character_count % 2 != 0:

        is_any_character_count_odd = True

print('Yes' if not is_any_character_count_odd else 'No')