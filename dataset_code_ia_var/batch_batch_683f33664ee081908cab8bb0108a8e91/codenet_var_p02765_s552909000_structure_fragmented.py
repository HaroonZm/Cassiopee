def get_input():
    return input()

def split_input(user_input):
    return user_input.split()

def convert_to_ints(strs):
    return (int(i) for i in strs)

def unpack_values(vals):
    n, r = vals
    return n, r

def check_greater_equal_10(n):
    return n >= 10

def calculate_result_case_true(r):
    return r

def calculate_result_case_false(n, r):
    return r + 100 * (10 - n)

def print_result(res):
    print(res)

def main():
    user_input = get_input()
    splitted = split_input(user_input)
    vals = convert_to_ints(splitted)
    n, r = unpack_values(vals)
    if check_greater_equal_10(n):
        res = calculate_result_case_true(r)
    else:
        res = calculate_result_case_false(n, r)
    print_result(res)

main()