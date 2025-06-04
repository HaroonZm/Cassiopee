import math

def get_input():
    return input()

def split_input(user_input):
    return user_input.split()

def map_to_ints(str_list):
    return map(int, str_list)

def get_a_b():
    user_input = get_input()
    splitted = split_input(user_input)
    return list(map_to_ints(splitted))

def compute_gcd(a, b):
    return math.gcd(a, b)

def divide_by_gcd(x, g):
    return x / g

def compute_a1(a, g):
    return divide_by_gcd(a, g)

def compute_b1(b, g):
    return divide_by_gcd(b, g)

def compute_expression(a1, b1, g):
    temp = a1 - 1 + b1
    return temp * g + 1

def print_result(result):
    print(int(result))

def main():
    values = get_a_b()
    a = values[0]
    b = values[1]
    g = compute_gcd(a, b)
    a1 = compute_a1(a, g)
    b1 = compute_b1(b, g)
    result = compute_expression(a1, b1, g)
    print_result(result)

main()