def input_values():
    return map(int, input().split())

def init_j(size):
    j = [1] + [0] * size
    return j

def init_k(size):
    k = [1] + [0] * size
    return k

def update_j(j, n):
    def helper(i):
        if i == 0:
            return
        j[i] = j[i-1] * 2 + 3
        helper(i-1)
    for i in range(1, n+1):
        j[i] = j[i-1] * 2 + 3

def update_k(k, n):
    def helper(i):
        if i == 0:
            return
        k[i] = k[i-1] * 2 + 1
        helper(i-1)
    for i in range(1, n+1):
        k[i] = k[i-1] * 2 + 1

def check_x_zero_or_negative(x):
    return x <= 0

def check_level_zero(level):
    return level == 0

def set_res_zero():
    return 0

def set_res_value(val):
    return val

def decrease_x(x):
    return x - 1

def more_than_j(x, j_value):
    return x > j_value

def adjust_x_and_res(x, j_val, k_val):
    x_new = x - j_val - 1
    res_new = k_val + 1
    return x_new, res_new

def sum_results(res, value):
    return res + value

def do(level, x):
    if check_x_zero_or_negative(x):
        return set_res_zero()
    if check_level_zero(level):
        return set_res_value(1)
    res = set_res_zero()
    x = decrease_x(x)
    if more_than_j(x, j[level-1]):
        x, add_res = adjust_x_and_res(x, j[level-1], k[level-1])
        res = sum_results(res, add_res)
    return sum_results(res, do(level-1, x))

def main():
    n, x = input_values()
    size = 50
    global j, k
    j = init_j(size)
    k = init_k(size)
    update_j(j, n)
    update_k(k, n)
    res = set_res_zero()
    print(do(n, x))

main()