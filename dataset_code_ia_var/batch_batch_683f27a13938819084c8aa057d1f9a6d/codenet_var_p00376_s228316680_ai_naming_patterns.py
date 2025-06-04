input_values = input().split()
int_values = list(map(int, input_values))
first_value = int_values[0]
second_value = int_values[1]
difference_value = abs(first_value - second_value)
print(difference_value)