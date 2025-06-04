def get_input_as_int():
    return int(input())

def is_one(value):
    return value == 1

def print_hello_world():
    print('Hello World')

def get_two_int_inputs():
    return int(input()), int(input())

def sum_values(a, b):
    return a + b

def print_sum(val):
    print(val)

def handle_case_one():
    print_hello_world()

def handle_case_else():
    a, b = get_two_int_inputs()
    total = sum_values(a, b)
    print_sum(total)

def execute_case(n):
    if is_one(n):
        handle_case_one()
    else:
        handle_case_else()

def main():
    n = get_input_as_int()
    execute_case(n)

if __name__ == '__main__':
    main()