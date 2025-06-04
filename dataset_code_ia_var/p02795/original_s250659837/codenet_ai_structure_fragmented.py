def read_H():
    return int(input())

def read_W():
    return int(input())

def read_N():
    return int(input())

def is_W_greater_equal_H(W, H):
    return W >= H

def compute_division(a, b):
    return a // b

def has_no_remainder(a, b):
    return a % b == 0

def print_result(value):
    print(value)

def process_case_divisible(div):
    print_result(div)

def process_case_not_divisible(div):
    print_result(div + 1)

def handle_W_greater_equal_H(N, W):
    div = compute_division(N, W)
    if has_no_remainder(N, W):
        process_case_divisible(div)
    else:
        process_case_not_divisible(div)

def handle_W_less_H(N, H):
    div = compute_division(N, H)
    if has_no_remainder(N, H):
        process_case_divisible(div)
    else:
        process_case_not_divisible(div)

def main():
    H = read_H()
    W = read_W()
    N = read_N()
    if is_W_greater_equal_H(W, H):
        handle_W_greater_equal_H(N, W)
    else:
        handle_W_less_H(N, H)

main()