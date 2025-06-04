def get_input():
    return input()

def parse_int(value):
    return int(value)

def read_int_from_input():
    return parse_int(get_input())

def is_one(n):
    return n == 1

def is_two(n):
    return n == 2

def print_hello_world():
    print("Hello World")

def add(a, b):
    return a + b

def print_sum(a, b):
    result = add(a, b)
    print(result)

def handle_case_one():
    print_hello_world()

def handle_case_two():
    a = read_int_from_input()
    b = read_int_from_input()
    print_sum(a, b)

def main():
    n = read_int_from_input()
    if is_one(n):
        handle_case_one()
    elif is_two(n):
        handle_case_two()

main()