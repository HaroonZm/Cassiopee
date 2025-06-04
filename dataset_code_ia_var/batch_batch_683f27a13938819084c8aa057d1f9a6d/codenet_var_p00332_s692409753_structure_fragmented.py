def get_input():
    return input()

def split_input(raw_input):
    return raw_input.split(" ")

def map_to_ints(str_list):
    return list(map(int, str_list))

def parse_input():
    raw_input = get_input()
    splitted = split_input(raw_input)
    return map_to_ints(splitted)

def is_e_0(e):
    return e == 0

def is_e_1(e):
    return e == 1

def is_e_2(e):
    return e == 2

def is_e_3(e):
    return e == 3

def is_e_4(e):
    return e == 4

def check_meiji(y):
    return y < 1912

def check_taisho(y):
    return y < 1926

def check_showa(y):
    return y < 1989

def print_meiji(y):
    print("M", y - 1867, sep='')

def print_taisho(y):
    print("T", y - 1911, sep='')

def print_showa(y):
    print("S", y - 1925, sep='')

def print_heisei(y):
    print("H", y - 1988, sep='')

def print_if_e_0(y):
    if check_meiji(y):
        print_meiji(y)
    elif check_taisho(y):
        print_taisho(y)
    elif check_showa(y):
        print_showa(y)
    else:
        print_heisei(y)

def add_meiji(y):
    return y + 1867

def add_taisho(y):
    return y + 1911

def add_showa(y):
    return y + 1925

def add_heisei(y):
    return y + 1988

def print_add_meiji(y):
    print(add_meiji(y))

def print_add_taisho(y):
    print(add_taisho(y))

def print_add_showa(y):
    print(add_showa(y))

def print_add_heisei(y):
    print(add_heisei(y))

def main():
    e, y = parse_input()
    if is_e_0(e):
        print_if_e_0(y)
    elif is_e_1(e):
        print_add_meiji(y)
    elif is_e_2(e):
        print_add_taisho(y)
    elif is_e_3(e):
        print_add_showa(y)
    elif is_e_4(e):
        print_add_heisei(y)

main()