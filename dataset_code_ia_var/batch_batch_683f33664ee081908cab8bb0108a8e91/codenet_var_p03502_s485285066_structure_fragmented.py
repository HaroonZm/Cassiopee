def get_input():
    return input()

def str_to_digits(s):
    return map(int, s)

def sum_digits(digits):
    return sum(digits)

def str_to_int(s):
    return int(s)

def is_divisible(number, divisor):
    return number % divisor == 0

def print_yes():
    print("Yes")

def print_no():
    print("No")

def check_divisibility_and_print():
    n = get_input()
    digits = str_to_digits(n)
    n_sum = sum_digits(digits)
    n_int = str_to_int(n)
    if is_divisible(n_int, n_sum):
        print_yes()
    else:
        print_no()

check_divisibility_and_print()