def read_input():
    return input().split()

def parse_input(inputs):
    return map(int, inputs)

def get_era_start_years():
    return [0, 1867, 1911, 1925, 1988]

def is_e_zero(e):
    return e == 0

def check_heisei(y):
    return y > 1988

def get_heisei_year(y):
    return f'H{y - 1988}'

def check_showa(y):
    return y > 1925

def get_showa_year(y):
    return f'S{y - 1925}'

def check_taisho(y):
    return y > 1911

def get_taisho_year(y):
    return f'T{y - 1911}'

def get_meiji_year(y):
    return f'M{y - 1867}'

def handle_e_zero(y):
    if check_heisei(y):
        print(get_heisei_year(y))
    elif check_showa(y):
        print(get_showa_year(y))
    elif check_taisho(y):
        print(get_taisho_year(y))
    else:
        print(get_meiji_year(y))

def handle_nonzero_e(e, y, ei):
    print(ei[e] + y)

def main():
    inputs = read_input()
    e, y = parse_input(inputs)
    ei = get_era_start_years()
    if is_e_zero(e):
        handle_e_zero(y)
    else:
        handle_nonzero_e(e, y, ei)

main()