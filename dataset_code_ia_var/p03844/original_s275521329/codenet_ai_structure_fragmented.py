def get_input():
    return input()

def split_input(user_input):
    return user_input.split()

def extract_first_operand(tokens):
    return tokens[0]

def extract_operator(tokens):
    return tokens[1]

def extract_second_operand(tokens):
    return tokens[2]

def convert_to_int(value):
    return int(value)

def add_operands(a, b):
    return a + b

def subtract_operands(a, b):
    return a - b

def print_result(result):
    print(result)

def process_operation():
    user_input = get_input()
    tokens = split_input(user_input)
    first_operand = extract_first_operand(tokens)
    operator = extract_operator(tokens)
    second_operand = extract_second_operand(tokens)
    a = convert_to_int(first_operand)
    b = convert_to_int(second_operand)
    if operator == '+':
        result = add_operands(a, b)
    else:
        result = subtract_operands(a, b)
    print_result(result)

process_operation()