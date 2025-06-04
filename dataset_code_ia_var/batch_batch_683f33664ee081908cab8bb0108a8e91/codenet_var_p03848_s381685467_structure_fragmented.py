import sys

def read_input():
    return int_input(), list_input()

def int_input():
    return int(input())

def list_input():
    return list(map(int, input().split()))

def sort_list(lst):
    return sorted(lst)

def is_odd(n):
    return n % 2 == 1

def is_even(n):
    return n % 2 == 0

def exit_with_zero():
    print(0)
    sys.exit()

def check_odd(A, n, mod):
    if A[0] != 0:
        exit_with_zero()
    for i in range(1, n // 2 + 1):
        check_odd_pair(A, i)
    return calculate_power(n // 2, mod)

def check_even(A, n, mod):
    for i in range(n // 2):
        check_even_pair(A, i)
    return calculate_power(n // 2, mod)

def check_odd_pair(A, i):
    if not (A[i * 2 - 1] == A[i * 2] == i * 2):
        exit_with_zero()

def check_even_pair(A, i):
    if not (A[i * 2] == A[i * 2 + 1] == i * 2 + 1):
        exit_with_zero()

def calculate_power(exp, mod):
    return pow(2, exp, mod)

def print_result(ans):
    print(ans)

def main():
    mod = 1000000007
    n, A = read_input()
    A = sort_list(A)
    if is_odd(n):
        ans = check_odd(A, n, mod)
    else:
        ans = check_even(A, n, mod)
    print_result(ans)

main()