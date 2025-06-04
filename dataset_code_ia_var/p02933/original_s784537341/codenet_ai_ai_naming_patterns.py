user_input_integer = int(input())
user_input_string = input()
threshold_value = 3200
output_string_if_above_threshold = user_input_string
output_string_if_below_threshold = 'red'

if user_input_integer >= threshold_value:
    print(output_string_if_above_threshold)
else:
    print(output_string_if_below_threshold)