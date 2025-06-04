import sys
from sys import stdin

def binary_fraction_formatter(input_float):
    UPPER_LIMIT = 256.0
    MULTIPLIER = 16
    BINARY_WIDTH_INTEGER = 8
    BINARY_WIDTH_FRACTION = 4

    if input_float >= UPPER_LIMIT:
        return 'NA'
    scaled_value = input_float * MULTIPLIER
    integer_scaled_value = int(scaled_value)
    if scaled_value != integer_scaled_value:
        return 'NA'
    binary_representation = bin(integer_scaled_value)[2:]
    fraction_bits = binary_representation[-BINARY_WIDTH_FRACTION:]
    integer_bits = binary_representation[:-BINARY_WIDTH_FRACTION]
    padded_integer_bits = integer_bits.zfill(BINARY_WIDTH_INTEGER)
    padded_fraction_bits = fraction_bits.zfill(BINARY_WIDTH_FRACTION)
    return padded_integer_bits + '.' + padded_fraction_bits

def process_input_stream(command_line_arguments):
    while True:
        input_line = stdin.readline()
        if not input_line:
            break
        try:
            parsed_float = float(input_line)
        except:
            continue
        if parsed_float < 0.0:
            break
        formatted_output = binary_fraction_formatter(parsed_float)
        print(formatted_output)

if __name__ == '__main__':
    process_input_stream(sys.argv[1:])