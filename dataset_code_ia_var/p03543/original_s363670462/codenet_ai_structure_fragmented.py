import sys

def read_input():
    return sys.stdin.readline().strip()

def get_digits():
    return "1234567890"

def repeat_char(c, n):
    return c * n

def check_substring_in_string(substring, string):
    return substring in string

def check_triple_in_string_for_char(x, c):
    triple = repeat_char(c, 3)
    return check_substring_in_string(triple, x)

def check_all_digits_for_triple(x):
    digits = get_digits()
    for c in digits:
        if check_triple_in_string_for_char(x, c):
            return True
    return False

def evaluate_and_print_result(x):
    if check_all_digits_for_triple(x):
        print("Yes")
    else:
        print("No")

def main():
    line = read_input()
    evaluate_and_print_result(line)

main()