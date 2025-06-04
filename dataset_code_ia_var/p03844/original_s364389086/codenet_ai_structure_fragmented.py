def get_input():
    return input()

def split_input(user_input):
    return [s for s in user_input.split()]

def extract_a(input_parts):
    return input_parts[0]

def extract_op(input_parts):
    return input_parts[1]

def extract_c(input_parts):
    return input_parts[2]

def is_addition(op):
    return op == "+"

def is_subtraction(op):
    return op == "-"

def to_int(s):
    return int(s)

def add_numbers(a, c):
    return a + c

def subtract_numbers(a, c):
    return a - c

def print_result(result):
    print(result)

def main():
    user_input = get_input()
    input_parts = split_input(user_input)
    a_str = extract_a(input_parts)
    op = extract_op(input_parts)
    c_str = extract_c(input_parts)
    a = to_int(a_str)
    c = to_int(c_str)
    if is_addition(op):
        result = add_numbers(a, c)
        print_result(result)
    elif is_subtraction(op):
        result = subtract_numbers(a, c)
        print_result(result)

main()