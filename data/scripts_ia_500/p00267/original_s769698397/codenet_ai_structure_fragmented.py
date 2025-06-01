def read_input():
    return input()

def read_and_sort_desc():
    numbers = read_numbers()
    return sort_desc(numbers)

def read_numbers():
    line = input()
    return list(map(int, line.split()))

def sort_desc(numbers):
    return sorted(numbers, reverse=True)

def should_break(user_input):
    return user_input == '0'

def process_lists(a, b):
    p = 0
    c = 0
    for i, x in enumerate(a):
        if i_div_2_less_than_c(i, c):
            print(i)
            return
        if x_less_equal_b_p(x, b, p):
            p = increment(p)
        else:
            c = increment(c)
    print_na()

def i_div_2_less_than_c(i, c):
    return i / 2 < c

def x_less_equal_b_p(x, b, p):
    if p < len(b):
        return x <= b[p]
    return False

def increment(value):
    return value + 1

def print_na():
    print('NA')

def main_loop():
    while True:
        user_input = read_input()
        if should_break(user_input):
            break
        a = read_and_sort_desc()
        b = read_and_sort_desc()
        process_lists(a, b)

main_loop()