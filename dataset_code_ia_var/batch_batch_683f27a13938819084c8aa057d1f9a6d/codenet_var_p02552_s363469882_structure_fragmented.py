def get_input():
    return input()

def convert_to_int(value):
    return int(value)

def is_zero(value):
    return value == 0

def is_one(value):
    return value == 1

def print_one():
    print(1)

def print_zero():
    print(0)

def handle_zero_case(value):
    if is_zero(value):
        print_one()

def handle_one_case(value):
    if is_one(value):
        print_zero()

def main_logic():
    user_input = get_input()
    value = convert_to_int(user_input)
    handle_zero_case(value)
    handle_one_case(value)

main_logic()