def read_input():
    return input()

def split_input(user_input):
    return user_input.split()

def map_to_int(str_numbers):
    return map(int, str_numbers)

def unpack_numbers(int_iterable):
    a, b, c = int_iterable
    return a, b, c

def compute_sum(a, b, c):
    return a + b + c

def is_bust(total):
    return total >= 22

def print_bust():
    print('bust')

def print_win():
    print('win')

def main():
    user_input = read_input()
    split_numbers = split_input(user_input)
    int_numbers = map_to_int(split_numbers)
    a, b, c = unpack_numbers(int_numbers)
    total = compute_sum(a, b, c)
    if is_bust(total):
        print_bust()
    else:
        print_win()

main()