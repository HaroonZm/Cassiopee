def get_input():
    return input()

def split_input(raw_input):
    return raw_input.split()

def str_to_ints(str_list):
    return list(map(int, str_list))

def assign_values(int_list):
    return int_list[0], int_list[1]

def compute_sum(a, b):
    return b + a

def decrement_one(value):
    return value - 1

def ceil_div(numerator, denominator):
    return (numerator + denominator - 1) // denominator

def main():
    raw_input = get_input()
    splitted = split_input(raw_input)
    int_values = str_to_ints(splitted)
    a, b = assign_values(int_values)
    s = compute_sum(a, b)
    d = decrement_one(s)
    result = ceil_div(d, a)
    print(result)

main()