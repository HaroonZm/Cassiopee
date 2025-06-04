input_value = int(input())
result_counter = 0
current_multiplier = 1
while 2 * current_multiplier - 1 <= input_value:
    current_multiplier = 2 * current_multiplier
    result_counter += 1
print(result_counter)