user_input_full = input()
user_input_partial = input()
user_input_partial_expected = user_input_partial[:-1]
result = 'Yes' if user_input_full == user_input_partial_expected else 'No'
print(result)