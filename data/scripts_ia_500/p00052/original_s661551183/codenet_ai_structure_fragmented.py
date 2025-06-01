import math

def read_integer():
    return int(input())

def is_zero(value):
    return value == 0

def compute_factorial(number):
    return math.factorial(number)

def convert_to_string_list(number):
    return list(str(number))

def count_trailing_zeros(digit_list):
    count = 0
    for digit in reversed(digit_list):
        if digit == "0":
            count += 1
        else:
            break
    return count

def print_count(count):
    print(count)

def main_loop():
    while True:
        n = read_integer()
        if is_zero(n):
            break
        factorial_value = compute_factorial(n)
        digit_list = convert_to_string_list(factorial_value)
        zero_count = count_trailing_zeros(digit_list)
        print_count(zero_count)

if __name__ == '__main__':
    main_loop()