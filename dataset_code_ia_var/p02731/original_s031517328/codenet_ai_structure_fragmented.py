def get_input():
    return input()

def to_int(value):
    return int(value)

def calculate_cube(value):
    return value * value * value

def divide_by_27(value):
    return value / 27

def print_result(result):
    print(result)

def main():
    user_input = get_input()
    int_value = to_int(user_input)
    cube = calculate_cube(int_value)
    divided = divide_by_27(cube)
    print_result(divided)

main()