def get_input():
    return input()

def convert_to_int(value):
    return int(value)

def divide_by_500(value):
    return value // 500

def multiply_by_500(value):
    return value * 500

def print_result(value):
    print(value)

def main():
    user_input = get_input()
    int_value = convert_to_int(user_input)
    quotient = divide_by_500(int_value)
    result = multiply_by_500(quotient)
    print_result(result)

main()