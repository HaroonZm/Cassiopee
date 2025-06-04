"""
Aizu Problem 0306: Symmetric Ternary Number

This script reads an integer N and converts it into a 'symmetric ternary' representation.
In this numeral system, each digit can be '+', '0', or '-', which correspond to +1, 0, or -1,
and each digit position is worth a power of 3 (as in ternary).

If the remainder (N % 3) is 2, we use '-', and increment N by 1 (to carry over like in negative base systems).
If the remainder is 1, we use '+'.
If the remainder is 0, we use '0'.
The result is constructed from least significant digit to most, so the final answer must be reversed.
"""

import sys
import os

def read_input():
    """
    Reads the integer input for the problem. If running in a development environment where
    the environment variable PYDEV is set to 'True', the input will be read from 'sample-input.txt'.
    Otherwise, input is read from standard input.
    
    Returns:
        int: The integer N to convert.
    """
    PYDEV = os.environ.get('PYDEV')
    if PYDEV == "True":
        sys.stdin = open("sample-input.txt", "rt")
    N = int(input())
    return N

def symmetric_ternary(N):
    """
    Converts an integer N into its symmetric ternary representation, where each digit is one of:
    '+' (representing +1), '0' (representing 0), or '-' (representing -1).

    The symmetric ternary representation is built from the least significant digit upwards,
    following these rules:
        - If N % 3 == 2, this digit is '-', increment N by 1
        - If N % 3 == 1, this digit is '+'
        - If N % 3 == 0, this digit is '0'

    Args:
        N (int): The integer to convert.

    Returns:
        str: The symmetric ternary representation as a string (most significant digit first).
    """
    if N == 0:
        return '0'
    result = ""
    while N > 0:
        remainder = N % 3
        if remainder == 2:
            result += '-'    # Using '-' for symmetric ternary -1
            N += 1           # Carry over: increment N as this is negative in value
        elif remainder == 1:
            result += '+'    # Using '+' for symmetric ternary +1
        else:
            result += '0'    # Using '0' for symmetric ternary 0
        N //= 3              # Move to next most significant digit
    return result[::-1]      # Reverse because digits were added least to most significant

def main():
    """
    Main execution function. Reads input and prints the symmetric ternary representation.
    """
    N = read_input()
    print(symmetric_ternary(N))

if __name__ == '__main__':
    main()