import sys
import math

input_stream = sys.stdin
output_stream = sys.stdout

input_value = int(input_stream.readline().strip())

current_sum = 1
current_power = 1

while True:
    if current_sum + current_power * 3 > input_value:
        break
    current_power *= 3
    current_sum += current_power * 2

result_counter = 1
remaining_value = input_value - 1

power_increment = 3
while power_increment < current_power:
    result_counter += 2
    remaining_value -= power_increment * 2
    power_increment *= 3
remaining_value -= current_power

division_power = current_power
while division_power:
    result_counter += remaining_value // division_power
    remaining_value -= (remaining_value // division_power) * division_power
    division_power //= 3

output_stream.writelines(str(result_counter + 1) + '\n')