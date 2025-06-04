def get_input():
    return input()

def split_input(user_input):
    return user_input.split()

def convert_to_int(str_list):
    return [int(i) for i in str_list]

def get_a(values):
    return values[0]

def get_b(values):
    return values[1]

def get_c(values):
    return values[2]

def is_c_in_range(a, b, c):
    return c >= a and c <= b

def print_yes():
    print("Yes")

def print_no():
    print("No")

def main():
    user_input = get_input()
    str_values = split_input(user_input)
    int_values = convert_to_int(str_values)
    a = get_a(int_values)
    b = get_b(int_values)
    c = get_c(int_values)
    if is_c_in_range(a, b, c):
        print_yes()
    else:
        print_no()

main()