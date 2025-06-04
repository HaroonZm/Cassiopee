def read_input():
    return input()

def split_input(user_input):
    return user_input.split()

def convert_to_ints(str_list):
    return [int(x) for x in str_list]

def get_n(vals):
    return vals[0]

def get_r(vals):
    return vals[1]

def compute_r_if_n_gt_10(n, r):
    return r

def compute_r_else(n, r):
    return r + 100 * (10 - n)

def should_use_regular_case(n):
    return n > 10

def calculate_R(n, r):
    if should_use_regular_case(n):
        return compute_r_if_n_gt_10(n, r)
    else:
        return compute_r_else(n, r)

def output_result(R):
    print(R)

def main():
    user_input = read_input()
    split_vals = split_input(user_input)
    n_r = convert_to_ints(split_vals)
    n = get_n(n_r)
    r = get_r(n_r)
    R = calculate_R(n, r)
    output_result(R)

main()