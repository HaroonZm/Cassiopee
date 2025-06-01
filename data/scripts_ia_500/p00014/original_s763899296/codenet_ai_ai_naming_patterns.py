import sys

def calculate_integral(square_input):
    return square_input ** 2

def compute_approximate_integral(step_size):
    total_sum = 0
    number_of_steps = int(600 / step_size)
    for step_index in range(1, number_of_steps):
        current_x = step_index * step_size
        total_sum += calculate_integral(current_x) * step_size
    return total_sum

for input_line in sys.stdin:
    input_step_size = int(input_line)
    result_value = compute_approximate_integral(input_step_size)
    print(result_value)