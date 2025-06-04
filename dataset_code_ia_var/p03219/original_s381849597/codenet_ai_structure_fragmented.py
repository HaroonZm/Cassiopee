def read_input():
    return input()

def split_input(s):
    return s.split()

def convert_to_ints(lst):
    return list(map(int, lst))

def extract_a_b(ints):
    return ints[0], ints[1]

def compute_b_half(b):
    return b / 2

def add_a_bhalf(a, b_half):
    return a + b_half

def convert_to_int(x):
    return int(x)

def print_result(result):
    print(result)

def main():
    user_input = read_input()
    splitted = split_input(user_input)
    ints = convert_to_ints(splitted)
    a, b = extract_a_b(ints)
    b_half = compute_b_half(b)
    sum_val = add_a_bhalf(a, b_half)
    result = convert_to_int(sum_val)
    print_result(result)

main()