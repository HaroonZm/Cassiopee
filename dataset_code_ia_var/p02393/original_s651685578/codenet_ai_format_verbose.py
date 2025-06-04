user_input_values = raw_input().split()

converted_integer_values = map(int, user_input_values)

sorted_integer_values = sorted(converted_integer_values)

smallest_value = sorted_integer_values[0]
middle_value = sorted_integer_values[1]
largest_value = sorted_integer_values[2]

print "%d %d %d" % (smallest_value, middle_value, largest_value)