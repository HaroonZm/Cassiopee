def get_input():
    return int(input())

def initialize_val(n):
    return n

def initialize_sum():
    return 0

def is_non_zero(val):
    return val != 0

def get_last_digit(val):
    return val % 10

def remove_last_digit(val):
    return val // 10

def add_to_sum(s, digit):
    return s + digit

def update_val(val):
    return remove_last_digit(val)

def is_divisible_by_sum(n, s):
    return n % s == 0

def print_yes():
    print("Yes")

def print_no():
    print("No")

def main():
    n = get_input()
    val = initialize_val(n)
    s = initialize_sum()
    while is_non_zero(val):
        digit = get_last_digit(val)
        s = add_to_sum(s, digit)
        val = update_val(val)
    if is_divisible_by_sum(n, s):
        print_yes()
    else:
        print_no()

main()