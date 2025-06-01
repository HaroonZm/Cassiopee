input_values = []
for index in range(5):
    input_values.append(int(input()))

total_value = 0
if input_values[0] < 0:
    total_value += (0 - input_values[0]) * input_values[2]
    total_value += input_values[3]
    total_value += input_values[1] * input_values[4]
elif input_values[0] > 0:
    total_value += (input_values[1] - input_values[0]) * input_values[4]

print(total_value)