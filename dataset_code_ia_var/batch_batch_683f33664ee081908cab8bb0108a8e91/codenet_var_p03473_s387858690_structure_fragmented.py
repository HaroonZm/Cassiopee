def get_input():
    return input()

def convert_to_int(value):
    return int(value)

def get_48():
    return 48

def subtract(a, b):
    return a - b

def print_result(result):
    print(result)

def main():
    user_input = get_input()
    int_value = convert_to_int(user_input)
    forty_eight = get_48()
    result = subtract(forty_eight, int_value)
    print_result(result)

main()