user_input_string = input()
user_input_set = set(user_input_string)
is_unique_characters = len(user_input_string) == len(user_input_set)
output_result = 'yes' if is_unique_characters else 'no'
print(output_result)