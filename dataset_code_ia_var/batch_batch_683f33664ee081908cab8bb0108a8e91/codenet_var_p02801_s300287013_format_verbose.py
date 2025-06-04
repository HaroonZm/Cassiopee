user_input_character = input()

unicode_code_point = ord(user_input_character)

next_unicode_code_point = unicode_code_point + 1

next_character = chr(next_unicode_code_point)

print(next_character)