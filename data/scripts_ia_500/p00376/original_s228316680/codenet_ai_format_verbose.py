input_values = input().split()

integer_values = list(map(int, input_values))

first_number = integer_values[0]
second_number = integer_values[1]

absolute_difference = abs(first_number - second_number)

print(absolute_difference)