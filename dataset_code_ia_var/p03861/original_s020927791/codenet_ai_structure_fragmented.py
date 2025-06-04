def get_input():
    return input()

def split_input(user_input):
    return user_input.split()

def map_to_int(str_list):
    return map(int, str_list)

def unpack_values(mapped_ints):
    return list(mapped_ints)

def parse_values():
    user_input = get_input()
    splitted = split_input(user_input)
    ints = map_to_int(splitted)
    vals = unpack_values(ints)
    return vals

def has_reached_minus_one(value):
    return value == -1

def floor_div(a, x):
    return a // x

def add_one(value):
    return value + 1

def compute_f(a, x):
    if has_reached_minus_one(a):
        return 0
    floored = floor_div(a, x)
    incremented = add_one(int(floored))
    return incremented

def decrement(value):
    return value - 1

def compute_result(a, b, x):
    first = compute_f(b, x)
    second = compute_f(decrement(a), x)
    return first - second

def output(result):
    print(result)

def main():
    values = parse_values()
    a, b, x = values
    result = compute_result(a, b, x)
    output(result)

main()