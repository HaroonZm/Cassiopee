def get_input():
    return input()

def split_input(inp):
    return inp.split()

def convert_to_int(str_list):
    return list(map(int, str_list))

def assign_values(int_list):
    return int_list[0], int_list[1], int_list[2]

def sum_values(a, b, c):
    return a + b + c

def is_bust(total):
    return total >= 22

def print_bust():
    print('bust')

def print_win():
    print('win')

def main():
    inp = get_input()
    splitted = split_input(inp)
    int_list = convert_to_int(splitted)
    a, b, c = assign_values(int_list)
    total = sum_values(a, b, c)
    if is_bust(total):
        print_bust()
    else:
        print_win()

main()