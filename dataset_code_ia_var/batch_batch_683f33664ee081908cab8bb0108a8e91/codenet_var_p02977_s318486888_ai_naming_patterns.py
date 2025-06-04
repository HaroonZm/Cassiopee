input_value = int(input())
output_func = print
range_func = range

if input_value & -input_value == input_value:
    output_func("No")
    exit(0)

output_func("Yes")

if input_value == 3:
    output_func(1, 2)
    output_func(2, 3)
    output_func(3, 4)
    output_func(4, 5)
    output_func(5, 6)
    exit(0)

max_power_two = 1
while max_power_two * 2 < input_value:
    max_power_two *= 2

for index in range_func(max_power_two - 2):
    output_func(index + 1, index + 2)

output_func(max_power_two - 1, input_value + 1)

for index in range_func(max_power_two - 2):
    output_func(input_value + index + 1, input_value + index + 2)

output_func(input_value + max_power_two, input_value + 1)
output_func(input_value + max_power_two + 1, max_power_two)

for index in range_func(input_value - max_power_two):
    output_func(input_value + index + 1, input_value + max_power_two + index + 1)
    output_func(input_value + max_power_two + index, max_power_two + index + 1)