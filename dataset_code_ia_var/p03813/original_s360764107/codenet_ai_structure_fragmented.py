def get_user_input():
    return input()

def convert_input_to_int(user_input):
    return int(user_input)

def is_less_than_1200(number):
    return number < 1200

def print_abc():
    print("ABC")

def print_arc():
    print("ARC")

def print_result(condition):
    if condition:
        print_abc()
    else:
        print_arc()

def main():
    user_input = get_user_input()
    num = convert_input_to_int(user_input)
    condition = is_less_than_1200(num)
    print_result(condition)

main()