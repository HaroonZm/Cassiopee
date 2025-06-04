def get_input():
    return input()

def split_input(user_input):
    return user_input.split()

def map_to_integers(split_values):
    return map(int, split_values)

def unpack_values(mapped):
    mapped = list(mapped)
    return mapped[0], mapped[1], mapped[2], mapped[3]

def calculate_result(n, a, b, c):
    return n - a - b + c

def print_result(result):
    print(result)

def main():
    user_input = get_input()
    split_values = split_input(user_input)
    mapped = map_to_integers(split_values)
    n, a, b, c = unpack_values(mapped)
    result = calculate_result(n, a, b, c)
    print_result(result)

main()