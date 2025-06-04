def get_input():
    return input()

def split_input(user_input):
    return user_input.split()

def str_list_to_int(lst):
    return [int(i) for i in lst]

def get_n_value(values):
    return values[0]

def get_r_value(values):
    return values[1]

def is_n_less_than_10(n):
    return n < 10

def compute_x(n):
    return 100 * (10 - n)

def sum_x_and_r(x, r):
    return x + r

def print_result(result):
    print(result)

def main():
    user_input = get_input()
    splitted = split_input(user_input)
    numbers = str_list_to_int(splitted)
    n = get_n_value(numbers)
    r = get_r_value(numbers)
    if is_n_less_than_10(n):
        x = compute_x(n)
        result = sum_x_and_r(x, r)
        print_result(result)
    else:
        print_result(r)

main()