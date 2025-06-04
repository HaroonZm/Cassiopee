def get_input():
    return input().split()

def to_int_list(str_list):
    return list(map(int, str_list))

def get_x(values):
    return values[0]

def get_y(values):
    return values[1]

def get_z(values):
    return values[2]

def get_d(values):
    return values[3]

def calc_abs(a, b):
    return abs(a - b)

def check_direct(x, z, d):
    return calc_abs(x, z) <= d

def check_indirect(x, y, z, d):
    return calc_abs(x, y) <= d and calc_abs(y, z) <= d

def output_yes():
    print("Yes")

def output_no():
    print("No")

def main():
    inp = get_input()
    values = to_int_list(inp)
    x = get_x(values)
    y = get_y(values)
    z = get_z(values)
    d = get_d(values)
    if check_direct(x, z, d):
        output_yes()
    elif check_indirect(x, y, z, d):
        output_yes()
    else:
        output_no()

main()