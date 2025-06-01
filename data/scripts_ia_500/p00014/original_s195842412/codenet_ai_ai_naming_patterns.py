import sys
for input_line in sys.stdin:
    divisor_value = int(input_line)
    accumulated_result = 0
    for multiple_value in range(divisor_value, 600 - divisor_value + 1, divisor_value):
        accumulated_result += divisor_value * multiple_value ** 2
    print(accumulated_result)