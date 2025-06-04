import sys
import numpy as np

read_entire_buffer = sys.stdin.buffer.read
read_line_buffer = sys.stdin.buffer.readline
read_lines_buffer = sys.stdin.buffer.readlines

MODULO = 10**9 + 7

number_of_iterations, sequence_length = map(int, read_entire_buffer().split())

def generate_power_sequence(base_value, sequence_size, modulo=MODULO):
    maximum_bit_length = sequence_size.bit_length()
    power_array = np.empty(1 << maximum_bit_length, np.int64)
    power_array[0] = 1
    temporary_base = base_value
    for bit_index in range(maximum_bit_length):
        range_start = 1 << bit_index
        range_end = 1 << (bit_index + 1)
        power_array[range_start:range_end] = power_array[:range_start] * temporary_base % modulo
        temporary_base = (temporary_base * temporary_base) % modulo
    power_array = power_array[:sequence_size]
    power_array.flags.writeable = False
    return power_array

powers_of_two_modulo = generate_power_sequence(2, sequence_length + 10)
inverse_powers_of_two_modulo = generate_power_sequence((1 + MODULO) // 2, sequence_length + 10)

def update_dynamic_programming_array(current_dp_array):
    previous_dp_array = current_dp_array.copy()
    
    weighted_terms = (
        current_dp_array *
        np.arange(sequence_length + 1) % MODULO *
        inverse_powers_of_two_modulo[:sequence_length + 1] % MODULO
    )
    
    cumulative_sum_weighted_terms = np.cumsum(weighted_terms[:-1]) % MODULO
    current_dp_array[1:] = cumulative_sum_weighted_terms
    current_dp_array[1:] = (current_dp_array[1:] * powers_of_two_modulo[:sequence_length]) % MODULO
    
    current_dp_array %= MODULO
    current_dp_array += np.arange(1, sequence_length + 2) * previous_dp_array
    current_dp_array %= MODULO

dynamic_programming_array = powers_of_two_modulo[:sequence_length + 1].copy()

for _ in range(number_of_iterations - 1):
    update_dynamic_programming_array(dynamic_programming_array)

print(dynamic_programming_array[-1])