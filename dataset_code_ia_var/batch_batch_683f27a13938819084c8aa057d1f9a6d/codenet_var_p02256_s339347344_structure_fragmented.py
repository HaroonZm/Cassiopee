import math

def get_input():
    return input()

def split_input(user_input):
    return user_input.split()

def convert_to_ints(str_list):
    return [int(i) for i in str_list]

def get_x_y(int_list):
    return int_list[0], int_list[1]

def compute_gcd(a, b):
    return math.gcd(a, b)

def display_result(result):
    print(result)

def main():
    user_input = get_input()
    str_list = split_input(user_input)
    int_list = convert_to_ints(str_list)
    x, y = get_x_y(int_list)
    result = compute_gcd(x, y)
    display_result(result)

main()