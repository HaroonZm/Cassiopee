from decimal import *
import sys
import copy

def set_precision():
    getcontext().prec = 1000

def read_input():
    return sys.stdin.readline

def parse_n_k(input_func):
    n, k = input_func().split()
    return int(n), Decimal(k)

def read_array(n, input_func):
    return [Decimal(input_func()) for _ in range(n)]

def contains_zero(a):
    return Decimal(0) in a

def handle_zero_case(n):
    print(n)
    sys.exit()

def is_k_zero(k):
    return k == Decimal(0)

def handle_k_zero_case():
    print(0)
    sys.exit()

def get_left_right(a):
    left = copy.copy(a)
    right = copy.copy(a)
    return left, right

def process_left(left):
    for i in range(len(left) - 1):
        left[i + 1] *= left[i]

def process_right(right):
    for i in reversed(range(len(right) - 1)):
        right[i] *= right[i + 1]

def get_total_mul(left):
    return left[-1]

def append_one(right):
    right.append(Decimal(1))

def build_r(right):
    result = []
    for i, x in enumerate(right):
        while result and result[-1][1] <= x:
            result.pop()
        result.append((i, x))
    return result

def build_l(left):
    result = [(-1, Decimal(1))]
    for i, x in enumerate(left):
        if not result or result[-1][1] < x:
            result.append((i, x))
    return result

def calc_ans(l, r, k, mul):
    ans = 0
    at = -1
    for i, x in l:
        while at + 1 < len(r) and x * r[at + 1][1] * k >= mul:
            at += 1
        if at >= 0 and ans < r[at][0] - i - 1:
            ans = r[at][0] - i - 1
    return ans

def print_result(ans):
    print(ans)

def main():
    set_precision()
    input_func = read_input()
    n, k = parse_n_k(input)
    a = read_array(n, input)
    if contains_zero(a):
        handle_zero_case(n)
    if is_k_zero(k):
        handle_k_zero_case()
    left, right = get_left_right(a)
    process_left(left)
    process_right(right)
    mul = get_total_mul(left)
    append_one(right)
    r = build_r(right)
    l = build_l(left)
    ans = calc_ans(l, r, k, mul)
    print_result(ans)

main()