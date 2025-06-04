def read_input():
    return input()

def split_input(s):
    return s.split()

def map_to_int(lst):
    return list(map(int, lst))

def assign_values(lst):
    return lst[0], lst[1], lst[2], lst[3]

def calc_ab_cd(a, b, c, d):
    return (a + b) - (c + d)

def calc_ac_bd(a, b, c, d):
    return (a + c) - (b + d)

def calc_ad_cb(a, b, c, d):
    return (a + d) - (c + b)

def abs_value(val):
    return abs(val)

def min_of_list(lst):
    return min(lst)

def print_result(val):
    print(val)

def main():
    s = read_input()
    splitted = split_input(s)
    ints = map_to_int(splitted)
    a, b, c, d = assign_values(ints)
    diff1 = abs_value(calc_ab_cd(a, b, c, d))
    diff2 = abs_value(calc_ac_bd(a, b, c, d))
    diff3 = abs_value(calc_ad_cb(a, b, c, d))
    min_diff = min_of_list([diff1, diff2, diff3])
    print_result(min_diff)

main()