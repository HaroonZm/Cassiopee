import sys

def read_input():
    return input()

def convert_to_int(s):
    return int(s)

def int_to_str(n):
    return str(n)

def get_length(s):
    return len(s)

def char_at(s, i):
    return s[i]

def char_to_int(c):
    return int(c)

def add(a, b):
    return a + b

def sum_digits(n_str):
    length = get_length(n_str)
    total = 0
    for i in range(length):
        digit_char = char_at(n_str, i)
        digit_int = char_to_int(digit_char)
        total = add(total, digit_int)
    return total

def is_divisible(a, b):
    return a % b == 0

def print_yes():
    print("Yes")

def print_no():
    print("No")

def process(n_input):
    n = convert_to_int(n_input)
    n_str = int_to_str(n)
    s = sum_digits(n_str)
    if is_divisible(n, s):
        print_yes()
    else:
        print_no()

def main():
    n_input = read_input()
    process(n_input)
    return

if __name__ == '__main__':
    main()