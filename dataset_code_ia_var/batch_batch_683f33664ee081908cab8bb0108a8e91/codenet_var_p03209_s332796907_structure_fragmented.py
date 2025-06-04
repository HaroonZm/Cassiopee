def read_input():
    return input().strip()

def str_to_int_list(s):
    return [int(x) for x in s.split()]

def generate_num_list():
    res = [1]
    for i in range(1, 51):
        res.append(2 * res[-1] + 3)
    return res

def generate_full_list():
    res = [1]
    for i in range(1, 51):
        res.append(2 * res[-1] + 1)
    return res

def f_dispatch(n, x, num, full):
    if n == 0:
        return f_case_zero()
    else:
        return f_cases(n, x, num, full)

def f_case_zero():
    return 1

def f_cases(n, x, num, full):
    if x == 1:
        return f_case_x_1()
    elif x <= num[n-1] + 1:
        return f_case_x_leq_half(n, x, num, full)
    elif x == num[n-1] + 2:
        return f_case_x_pivot(n, num, full)
    elif x == num[n]:
        return f_case_x_max(n, num, full)
    else:
        return f_case_general(n, x, num, full)

def f_case_x_1():
    return 0

def f_case_x_leq_half(n, x, num, full):
    return f_dispatch(n-1, x-1, num, full)

def f_case_x_pivot(n, num, full):
    return 1 + full[n-1]

def f_case_x_max(n, num, full):
    return 1 + 2 * full[n-1]

def f_case_general(n, x, num, full):
    return 1 + full[n-1] + f_dispatch(n-1, x-2-num[n-1], num, full)

def main():
    s = read_input()
    input_vals = str_to_int_list(s)
    N, X = input_vals[0], input_vals[1]
    num = generate_num_list()
    full = generate_full_list()
    result = f_dispatch(N, X, num, full)
    print(result)

main()