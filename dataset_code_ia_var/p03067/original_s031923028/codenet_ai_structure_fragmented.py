def get_input():
    return input()

def split_input(user_input):
    return user_input.split()

def map_to_int(str_values):
    return map(int, str_values)

def unpack_values(mapped_values):
    values = list(mapped_values)
    return values[0], values[1], values[2]

def is_middle(a, b, c):
    return (a < c < b) or (a > c > b)

def get_yes_no(condition):
    if condition:
        return "Yes"
    else:
        return "No"

def print_result(result):
    print(result)

def main():
    user_input = get_input()
    str_values = split_input(user_input)
    mapped_values = map_to_int(str_values)
    A, B, C = unpack_values(mapped_values)
    condition = is_middle(A, B, C)
    result = get_yes_no(condition)
    print_result(result)

main()