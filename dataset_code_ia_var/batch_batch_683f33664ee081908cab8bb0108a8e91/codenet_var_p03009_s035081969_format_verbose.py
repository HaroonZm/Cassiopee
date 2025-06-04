number_of_elements, max_height, window_size = map(int, input().split())

MODULO_DIVISOR = 10 ** 9 + 7
factorial_accumulator = 1
cumulative_sum = 0

for element_index in range(1, number_of_elements + 1):
    factorial_accumulator = (factorial_accumulator * element_index) % MODULO_DIVISOR
    cumulative_sum = (cumulative_sum + factorial_accumulator) % MODULO_DIVISOR

window_values = [factorial_accumulator]
current_accumulator = factorial_accumulator

for height in range(1, max_height):
    next_window_value = (current_accumulator * cumulative_sum) % MODULO_DIVISOR
    window_values.append(next_window_value)
    current_accumulator = (current_accumulator + window_values[-1]) % MODULO_DIVISOR
    if height >= window_size:
        current_accumulator = (current_accumulator - window_values[-window_size - 1]) % MODULO_DIVISOR

print(current_accumulator)