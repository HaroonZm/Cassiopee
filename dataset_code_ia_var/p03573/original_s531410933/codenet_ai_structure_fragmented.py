def read_input():
    return input()

def split_input(user_input):
    return user_input.split()

def convert_to_int(str_values):
    return list(map(int, str_values))

def get_A(values):
    return values[0]

def get_B(values):
    return values[1]

def get_C(values):
    return values[2]

def is_equal(x, y):
    return x == y

def print_value(value):
    print(value)

def handle_A_equals_B(A, B, C):
    if is_equal(A, B):
        print_value(C)
        return True
    return False

def handle_A_equals_C(A, B, C):
    if is_equal(A, C):
        print_value(B)
        return True
    return False

def handle_B_equals_C(A, B, C):
    if is_equal(B, C):
        print_value(A)
        return True
    return False

def main():
    user_input = read_input()
    splitted = split_input(user_input)
    int_values = convert_to_int(splitted)
    A = get_A(int_values)
    B = get_B(int_values)
    C = get_C(int_values)
    if handle_A_equals_B(A, B, C):
        return
    if handle_A_equals_C(A, B, C):
        return
    if handle_B_equals_C(A, B, C):
        return

main()