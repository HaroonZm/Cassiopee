def get_input():
    return input()

def convert_to_int(value):
    return int(value)

def check_zero(value):
    return value == 0

def check_one(value):
    return value == 1

def print_one():
    print("1")

def print_zero():
    print("0")

def process_value(value):
    if check_zero(value):
        print_one()
    if check_one(value):
        print_zero()

def main():
    user_input = get_input()
    int_value = convert_to_int(user_input)
    process_value(int_value)

main()