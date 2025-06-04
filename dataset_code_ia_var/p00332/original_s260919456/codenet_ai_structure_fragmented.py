def get_input():
    return input()

def parse_input(raw_input):
    return map(int, raw_input.split())

def is_era_input(E):
    return E == 0

def era_m(Y):
    return 1868 <= Y <= 1911

def era_t(Y):
    return 1912 <= Y <= 1925

def era_s(Y):
    return 1926 <= Y <= 1988

def era_h(Y):
    return Y >= 1989

def convert_m(Y):
    return "M" + str(Y - 1868 + 1)

def convert_t(Y):
    return "T" + str(Y - 1912 + 1)

def convert_s(Y):
    return "S" + str(Y - 1926 + 1)

def convert_h(Y):
    return "H" + str(Y - 1989 + 1)

def convert_era(E, Y):
    if is_era_input(E):
        if era_m(Y):
            return convert_m(Y)
        elif era_t(Y):
            return convert_t(Y)
        elif era_s(Y):
            return convert_s(Y)
        else:
            return convert_h(Y)
    else:
        return convert_ad_to_era(E, Y)

def convert_ad_to_era(E, Y):
    if E == 1:
        return 1868 + Y - 1
    elif E == 2:
        return 1912 + Y - 1
    elif E == 3:
        return 1926 + Y - 1
    else:
        return 1989 + Y - 1

def print_result(result):
    print(result)

def main():
    raw_input = get_input()
    E, Y = parse_input(raw_input)
    result = convert_era(E, Y)
    print_result(result)

main()