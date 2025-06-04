def get_first_input():
    return input()

def convert_to_int(value):
    return int(value)

def is_one(value):
    return value == 1

def get_second_input():
    return input()

def get_third_input():
    return input()

def compute_sum(a, b):
    return a + b

def print_result(result):
    print(result)

def process_branch_one():
    print_result("Hello World")

def process_branch_two():
    second = convert_to_int(get_second_input())
    third = convert_to_int(get_third_input())
    result = compute_sum(second, third)
    print_result(result)

def main():
    first_input = get_first_input()
    first_value = convert_to_int(first_input)
    if is_one(first_value):
        process_branch_one()
    else:
        process_branch_two()

main()