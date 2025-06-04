def get_input():
    return input()

def split_input(inp):
    return inp.split()

def convert_to_int(str_list):
    return list(map(int, str_list))

def assign_variables(int_list):
    return int_list[0], int_list[1]

def compute_difference(a, b):
    return a - (2 * b)

def check_negative(value):
    return value < 0

def print_zero():
    print(0)

def print_value(value):
    print(value)

def main():
    inp = get_input()
    split_inp = split_input(inp)
    int_list = convert_to_int(split_inp)
    a, b = assign_variables(int_list)
    diff = compute_difference(a, b)
    if check_negative(diff):
        print_zero()
    else:
        print_value(diff)

main()