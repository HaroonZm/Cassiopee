user_input_string = input()

first_character = user_input_string[0]
last_character = user_input_string[-1]
string_length = len(user_input_string)

characters_are_equal = (first_character == last_character)

result_index = (string_length + characters_are_equal) % 2

winner_names = ['Second', 'First']

print(winner_names[result_index])