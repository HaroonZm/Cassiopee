def get_input():
    return input()

def split_input(s):
    return s.split()

def convert_to_int_list(str_list):
    return list(map(int, str_list))

def parse_input():
    s = get_input()
    str_list = split_input(s)
    int_list = convert_to_int_list(str_list)
    return int_list

def is_between(a, b, c):
    return a <= c and c <= b

def is_between_reversed(a, b, c):
    return b <= c and c <= a

def print_yes():
    print('Yes')

def print_no():
    print('No')

def decide_and_print(l):
    if is_between(l[0], l[1], l[2]):
        print_yes()
    elif is_between_reversed(l[0], l[1], l[2]):
        print_yes()
    else:
        print_no()

def main():
    l = parse_input()
    decide_and_print(l)

main()