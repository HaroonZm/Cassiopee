def read_input():
    return input()

def parse_input(s):
    return s.split()

def convert_to_ints(lst):
    return list(map(int, lst))

def get_a_b():
    s = read_input()
    lst = parse_input(s)
    ints = convert_to_ints(lst)
    return ints[0], ints[1]

def compute_b_times_2(b):
    return b * 2

def compute_difference(a, val):
    return a - val

def clamp_min_zero(x):
    return max(0, x)

def process():
    a, b = get_a_b()
    b2 = compute_b_times_2(b)
    diff = compute_difference(a, b2)
    result = clamp_min_zero(diff)
    print_result(result)

def print_result(res):
    print(res)

if __name__ == '__main__':
    process()