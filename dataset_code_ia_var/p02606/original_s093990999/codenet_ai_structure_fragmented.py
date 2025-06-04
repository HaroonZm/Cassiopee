def read_inputs():
    return input().split()

def convert_to_ints(str_list):
    return list(map(int, str_list))

def get_L(values):
    return values[0]

def get_R(values):
    return values[1]

def get_d(values):
    return values[2]

def compute_L_mod_d(L, d):
    return L % d

def is_L_divisible(L_mod_d):
    return L_mod_d == 0

def integer_division(a, b):
    return int(a / b)

def compute_count_case1(R, d, L, d2):
    return integer_division(R, d) - integer_division(L, d2) + 1

def compute_count_case2(R, d, L, d2):
    return integer_division(R, d) - integer_division(L, d2)

def main():
    raw_inputs = read_inputs()
    int_values = convert_to_ints(raw_inputs)
    L = get_L(int_values)
    R = get_R(int_values)
    d = get_d(int_values)
    L_mod_d = compute_L_mod_d(L, d)
    if is_L_divisible(L_mod_d):
        result = compute_count_case1(R, d, L, d)
    else:
        result = compute_count_case2(R, d, L, d)
    print(result)

main()