def get_input():
    return input().split()

def to_ints(str_list):
    return list(map(int, str_list))

def get_L_X():
    inputs = get_input()
    ints = to_ints(inputs)
    return ints[0], ints[1]

def base_h_case(l):
    return l == 0

def h_rec(l):
    return h(l - 1) * 2 + 3

def h(l):
    if base_h_case(l):
        return 1
    else:
        return h_rec(l)

def base_f_case(l):
    return l == 0

def x_is_zero(x):
    return x == 0

def f_base_case(x):
    if x_is_zero(x):
        return 0
    else:
        return 1

def f_left_side(l, x):
    return f(l - 1, x - 1)

def x_leq_one(x):
    return x <= 1

def f_leq_h_minus_one(l):
    return f(l - 1, h(l - 1))

def x_within_first_half(l, x):
    return x <= h(l - 1) + 1

def x_equals_mid(l, x):
    return x == h(l - 1) + 2

def f_mid(l):
    return f_leq_h_minus_one(l) + 1

def x_within_second_half(l, x):
    return x <= h(l - 1) * 2 + 2

def f_right_side(l, x):
    return f_leq_h_minus_one(l) + 1 + f(l - 1, x - h(l - 1) - 2)

def f_last_case(l):
    return f_leq_h_minus_one(l) * 2 + 1

def f(l, x):
    if base_f_case(l):
        return f_base_case(x)
    if x_leq_one(x):
        return 0
    if x_within_first_half(l, x):
        return f_left_side(l, x)
    if x_equals_mid(l, x):
        return f_mid(l)
    if x_within_second_half(l, x):
        return f_right_side(l, x)
    return f_last_case(l)

def main():
    L, X = get_L_X()
    print(f(L, X))

main()