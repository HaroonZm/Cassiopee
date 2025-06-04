user_input_string = input()

unique_characters_in_input = set(user_input_string)

are_all_characters_unique = len(user_input_string) == len(unique_characters_in_input)

if are_all_characters_unique:
    print('yes')
else:
    print('no')