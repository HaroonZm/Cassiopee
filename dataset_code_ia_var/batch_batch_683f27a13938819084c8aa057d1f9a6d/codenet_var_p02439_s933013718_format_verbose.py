input_values_as_strings = input().split()

input_values_as_integers = list(map(int, input_values_as_strings))

minimum_value_in_input = min(input_values_as_integers)

maximum_value_in_input = max(input_values_as_integers)

print(minimum_value_in_input, maximum_value_in_input)