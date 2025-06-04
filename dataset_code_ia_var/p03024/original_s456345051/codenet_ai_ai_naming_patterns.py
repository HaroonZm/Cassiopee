#!/usr/bin/env python3

def process_input_check_x_count():
    input_string = input()
    x_char_count = input_string.count('x')
    minimum_required_x_count = 8
    if x_char_count < minimum_required_x_count:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    process_input_check_x_count()