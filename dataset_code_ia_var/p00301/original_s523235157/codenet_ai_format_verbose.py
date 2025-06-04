import sys
import math
import os

# Handle development environment for input redirection
is_pydev_environment = os.environ.get('PYDEV')

if is_pydev_environment == "True":
    sys.stdin = open("sample-input.txt", "rt")

input_decimal_number = int(input())

symmetric_ternary_representation = ""

while input_decimal_number > 0:

    current_remainder = input_decimal_number % 3

    if current_remainder == 2:
        symmetric_ternary_representation += '-'
        input_decimal_number += 1
    elif current_remainder == 1:
        symmetric_ternary_representation += '+'
    else:
        symmetric_ternary_representation += '0'

    input_decimal_number //= 3

reversed_symmetric_ternary = symmetric_ternary_representation[::-1]

print(reversed_symmetric_ternary)