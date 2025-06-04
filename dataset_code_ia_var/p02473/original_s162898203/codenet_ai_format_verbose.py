user_input_string = input()

user_input_with_hyphens = user_input_string.replace(" ", "-")

evaluated_result = eval(user_input_with_hyphens)

print(evaluated_result)