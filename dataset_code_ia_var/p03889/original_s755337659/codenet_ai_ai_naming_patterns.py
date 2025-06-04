user_input = input()
mirror_map = str.maketrans({'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'})
reversed_user_input = user_input[::-1]
mirrored_reversed_input = reversed_user_input.translate(mirror_map)
result_output = "Yes" if user_input == mirrored_reversed_input else "No"
print(result_output)