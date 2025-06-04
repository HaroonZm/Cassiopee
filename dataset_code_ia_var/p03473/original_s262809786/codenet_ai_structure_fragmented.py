def get_input():
    return input()

def to_int(value):
    return int(value)

def calc_24_minus_a(a):
    return 24 - a

def add_24(value):
    return value + 24

def print_result(result):
    print(result)

def main():
    user_input = get_input()
    int_value = to_int(user_input)
    subtracted = calc_24_minus_a(int_value)
    total = add_24(subtracted)
    print_result(total)

main()