def get_input():
    return input()

def convert_to_int(s):
    return int(s)

def divide_by_three(n):
    return n / 3

def power_of_three(n):
    return n ** 3

def print_result(res):
    print(res)

def main():
    value_str = get_input()
    value_int = convert_to_int(value_str)
    divided = divide_by_three(value_int)
    result = power_of_three(divided)
    print_result(result)

main()