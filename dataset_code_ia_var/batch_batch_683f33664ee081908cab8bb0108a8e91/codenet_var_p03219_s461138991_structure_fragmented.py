def get_input():
    return input()

def split_input(user_input):
    return user_input.split()

def str_to_int(str_values):
    return list(map(int, str_values))

def extract_x(int_values):
    return int_values[0]

def extract_y(int_values):
    return int_values[1]

def divide_by_two(y):
    return y // 2

def sum_x_and_half_y(x, y_half):
    return x + y_half

def print_result(result):
    print(result)

def main():
    user_input = get_input()
    split_values = split_input(user_input)
    int_values = str_to_int(split_values)
    x = extract_x(int_values)
    y = extract_y(int_values)
    y_half = divide_by_two(y)
    result = sum_x_and_half_y(x, y_half)
    print_result(result)

main()