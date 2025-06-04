import sys

standard_input_buffer = sys.stdin.buffer
read_entire_input = standard_input_buffer.read
read_single_line = standard_input_buffer.readline
read_all_lines = standard_input_buffer.readlines

# The function adjusts the value depending on even/odd status

total_value, percentage_parameter = map(int, read_entire_input().split())

def calculate_value(input_value):
    half_value = input_value // 2
    return (half_value * 100) / percentage_parameter

if total_value % 2 == 0:
    computed_result = calculate_value(total_value)
else:
    computed_result = (
        1
        + (
            percentage_parameter * calculate_value(total_value - 1)
            + (100 - percentage_parameter) * calculate_value(total_value + 1)
        )
        / 100
    )

print(computed_result)