def read_input():
    return input().strip()

def string_to_int(s):
    return int(s)

def initialize_sum():
    return 0

def digit_generator(s):
    for ch in s:
        yield ch

def char_to_int(ch):
    return int(ch)

def add_to_sum(total, value):
    return total + value

def compute_digit_sum(s):
    total = initialize_sum()
    for ch in digit_generator(s):
        value = char_to_int(ch)
        total = add_to_sum(total, value)
    return total

def is_divisible(n, digit_sum):
    return n % digit_sum == 0

def result_string(is_yes):
    return "Yes" if is_yes else "No"

def main():
    ss = read_input()
    n = string_to_int(ss)
    digit_sum = compute_digit_sum(ss)
    divisible = is_divisible(n, digit_sum)
    result = result_string(divisible)
    print(result)

main()