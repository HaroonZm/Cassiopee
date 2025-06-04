def get_input():
    return input()

def split_input(data):
    return data.split()

def parse_operand(operand):
    return int(operand)

def get_first_operand(parts):
    return parts[0]

def get_operator(parts):
    return parts[1]

def get_second_operand(parts):
    return parts[2]

def perform_addition(a, b):
    return a + b

def perform_subtraction(a, b):
    return a - b

def is_addition(op):
    return op == "+"

def print_result(result):
    print(result)

def main():
    data = get_input()
    parts = split_input(data)
    a_str = get_first_operand(parts)
    b_str = get_second_operand(parts)
    op = get_operator(parts)
    a = parse_operand(a_str)
    b = parse_operand(b_str)
    if is_addition(op):
        res = perform_addition(a, b)
    else:
        res = perform_subtraction(a, b)
    print_result(res)

main()