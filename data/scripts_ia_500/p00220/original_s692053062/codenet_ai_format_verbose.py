import sys
from sys import stdin
input = stdin.readline


def convert_float_to_fixed_point_representation(float_number):
    
    if float_number >= 256.0:
        return 'NA'
    
    scaled_value = float_number * 16
    integer_scaled_value = int(scaled_value)
    
    if scaled_value != integer_scaled_value:
        return 'NA'
    
    binary_representation = bin(integer_scaled_value)[2:]
    
    fractional_part_binary = binary_representation[-4:]
    integer_part_binary = binary_representation[:-4]
    
    padded_integer_part = integer_part_binary.zfill(8)
    padded_fractional_part = fractional_part_binary.zfill(4)
    
    return padded_integer_part + '.' + padded_fractional_part


def main(arguments):
    
    while True:
        input_line = input()
        float_value = float(input_line)
        
        if float_value < 0.0:
            break
        
        fixed_point_result = convert_float_to_fixed_point_representation(float_value)
        print(fixed_point_result)


if __name__ == '__main__':
    main(sys.argv[1:])