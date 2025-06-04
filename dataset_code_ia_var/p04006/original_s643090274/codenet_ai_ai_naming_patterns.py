input_values = list(map(int, open(0).read().split()))
input_count = input_values[0]
increment_value = input_values[1]
array_values = input_values[2:]

minimum_total = 10**18

for iteration_index in range(input_count):
    current_total = sum(array_values) + increment_value * iteration_index
    minimum_total = min(minimum_total, current_total)
    updated_array = []
    for value_index in range(len(array_values)):
        previous_index = (value_index - 1) % len(array_values)
        updated_value = min(array_values[value_index], array_values[previous_index])
        updated_array.append(updated_value)
    array_values = updated_array

print(minimum_total)