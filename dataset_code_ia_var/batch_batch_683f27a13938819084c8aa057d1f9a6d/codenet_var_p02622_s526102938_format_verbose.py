first_input_string_characters_list = list(str(input()).lower())

second_input_string_characters_list = list(str(input()).lower())

number_of_different_characters = 0

for character_index in range(0, len(first_input_string_characters_list)):

    if first_input_string_characters_list[character_index] != second_input_string_characters_list[character_index]:
    
        number_of_different_characters += 1

print(number_of_different_characters)