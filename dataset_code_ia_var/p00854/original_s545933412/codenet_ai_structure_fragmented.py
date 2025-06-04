import sys

def get_raw_input():
    if sys.version_info[0] >= 3:
        return input
    else:
        return raw_input

def get_input_values(raw_input_func):
    return [int(e) for e in raw_input_func().split()]

def should_break(n):
    return n == 0

def initialize_r():
    return 0

def update_r(r, k, i):
    return (r + k) % i

def loop_range(n):
    return range(1, n)

def compute_final_result(r, m, n):
    return (r + m) % n + 1

def process_one_case(n, k, m):
    r = initialize_r()
    for i in loop_range(n):
        r = update_r(r, k, i)
    return compute_final_result(r, m, n)

def main_loop():
    raw_input_func = get_raw_input()
    while True:
        n, k, m = get_input_values(raw_input_func)
        if should_break(n):
            break
        result = process_one_case(n, k, m)
        print(result)

main_loop()