def read_input():
    return int(input())

def read_amida_line():
    return list(map(int, input().split()))

def process_amida_line(amida_line):
    return amida_line[1:]

def initialize_res():
    return [0, 1, 2]

def swap_res(res, i):
    if i:
        return swap1(res)
    else:
        return swap0(res)

def swap1(res):
    copy_res = res[:]
    copy_res[1], copy_res[2] = copy_res[2], copy_res[1]
    return copy_res

def swap0(res):
    copy_res = res[:]
    copy_res[0], copy_res[1] = copy_res[1], copy_res[0]
    return copy_res

def amida():
    amida_line = read_amida_line()
    line = process_amida_line(amida_line)
    res = initialize_res()
    for i in line:
        res = swap_res(res, i)
    return res

def toint(x):
    return x[0]*9 + x[1]*3 + x[2]

def tolist(x):
    a = x // 9
    b = x % 9 // 3
    c = x % 3
    return [a, b, c]

def initialize_aa():
    return [0 for _ in range(27)]

def process_amidas(amidas, aa):
    for i in amidas:
        idx = toint(i)
        increment_aa(aa, idx)

def increment_aa(aa, idx):
    aa[idx] += 1

def is_initial(line):
    return line == [0, 1, 2]

def apply_swaps(line, swaps):
    return [line[swaps[0]], line[swaps[1]], line[swaps[2]]]

def func(x, line, flag):
    if check_func_base_case(line, flag):
        return True
    return func_iterate(x, line, flag)

def check_func_base_case(line, flag):
    return is_initial(line) and flag

def func_iterate(x, line, flag):
    for i in range(27):
        if should_continue_func(x, i): continue
        swaps = tolist(i)
        x[i] -= 1
        res = func(x, apply_swaps(line, swaps), True)
        x[i] += 1
        if res:
            return True
    return False

def should_continue_func(x, i):
    return x[i] == 0

def check_quick_solution(aa):
    for i in range(27):
        if aa[i] == 0: continue
        line = [0, 1, 2]
        for j in range(aa[i]):
            swaps = tolist(i)
            line = apply_swaps(line, swaps)
            if is_initial(line):
                return True
    return False

def main():
    n = read_input()
    if check_n_big(n):
        print_yes_and_exit()
    amidas = []
    for _ in range(n):
        amidas.append(amida())
    aa = initialize_aa()
    process_amidas(amidas, aa)
    if check_quick_solution(aa):
        print_yes_and_exit()
    if func(aa, [0, 1, 2], False):
        print_yes_and_exit()
    print("no")

def check_n_big(n):
    return n >= 7

def print_yes_and_exit():
    print("yes")
    exit()

main()