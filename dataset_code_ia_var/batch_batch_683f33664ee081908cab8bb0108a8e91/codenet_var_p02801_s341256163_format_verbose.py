user_input_character = input()

unicode_code_point_of_input = ord(user_input_character)

unicode_code_point_of_next_character = unicode_code_point_of_input + 1

next_character = chr(unicode_code_point_of_next_character)

print(next_character)