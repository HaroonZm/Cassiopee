def read_input():
    return input()

def parse_int(value):
    return int(value)

def int_to_str(n):
    return str(n)

def str_to_list(s):
    return list(s)

def list_digits(str_list):
    return [parse_int(char) for char in str_list]

def sum_digits(digits_list):
    total = 0
    for digit in digits_list:
        total += digit
    return total

def is_divisible(n, s):
    return n % s == 0

def print_yes():
    print('Yes')

def print_no():
    print('No')

def main():
    n_str = read_input()
    n = parse_int(n_str)
    s_str = int_to_str(n)
    s_list = str_to_list(s_str)
    digits = list_digits(s_list)
    s = sum_digits(digits)
    if is_divisible(n, s):
        print_yes()
    else:
        print_no()

main()