def get_meiji_year(y):
    return 'M' + str(y - 1868 + 1)

def get_taisho_year(y):
    return 'T' + str(y - 1912 + 1)

def get_showa_year(y):
    return 'S' + str(y - 1926 + 1)

def get_heisei_year(y):
    return 'H' + str(y - 1989 + 1)

def select_japanese_era(y):
    if y < 1912:
        return get_meiji_year(y)
    elif y < 1926:
        return get_taisho_year(y)
    elif y < 1989:
        return get_showa_year(y)
    else:
        return get_heisei_year(y)

def get_starting_years_list():
    return [0, 1868, 1912, 1926, 1989]

def calculate_year_from_era_index(e, y):
    yy = get_starting_years_list()
    base_year = yy[e]
    return base_year + y - 1

def solve(e, y):
    if e == 0:
        result = select_japanese_era(y)
    else:
        result = calculate_year_from_era_index(e, y)
    return result

def read_input():
    input_str = input()
    return parse_input(input_str)

def parse_input(input_str):
    E, Y = map(int, input_str.split())
    return E, Y

def display_result(result):
    print(result)

def main():
    E, Y = read_input()
    result = solve(E, Y)
    display_result(result)

if __name__ == '__main__':
    main()