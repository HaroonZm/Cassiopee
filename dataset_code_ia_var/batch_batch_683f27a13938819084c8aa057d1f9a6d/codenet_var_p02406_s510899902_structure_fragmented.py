def get_input():
    return int(input())

def is_divisible_by_three(x):
    return x % 3 == 0

def has_digit_three(x):
    return contains_digit(x, 3)

def contains_digit(x, digit):
    while x > 0:
        if x % 10 == digit:
            return True
        x //= 10
    return False

def print_number(i):
    print("", i, end="")

def process_number(i):
    if check_and_print_if_divisible_by_three(i):
        return
    check_and_print_if_contains_digit_three(i)

def check_and_print_if_divisible_by_three(i):
    if is_divisible_by_three(i):
        print_number(i)
        return True
    return False

def check_and_print_if_contains_digit_three(i):
    if has_digit_three(i):
        print_number(i)

def range_inclusive(start, end):
    return range(start, end + 1)

def main_loop(n):
    for i in range_inclusive(1, n):
        process_number(i)
    print("")

def main():
    n = get_input()
    main_loop(n)

if __name__ == "__main__":
    main()