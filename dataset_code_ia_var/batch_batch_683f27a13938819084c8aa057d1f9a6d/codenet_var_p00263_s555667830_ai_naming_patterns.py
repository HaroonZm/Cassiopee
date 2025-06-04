bin_values = [0] * 32

current_integer_power = 1
for bin_index in range(24, 0, -1):
    bin_values[bin_index] = current_integer_power
    current_integer_power *= 2

current_fractional_power = 0.5
for bin_index in range(25, 32):
    bin_values[bin_index] = current_fractional_power
    current_fractional_power /= 2

query_count = int(input())

for query_index in range(query_count):
    hex_input = input()
    binary_string = format(int(hex_input, 16), 'b').zfill(32)
    result_value = 0.0
    for bit_position, bit_char in enumerate(binary_string[1:]):
        result_value += bin_values[bit_position + 1] * int(bit_char)
    sign_prefix = '-' if binary_string[0] == '1' else ''
    print(f"{sign_prefix}{result_value}")