import math

def read_input():
    return map(int, input().split())

def compute_absolute_difference(a, b):
    return abs(a - b)

def numbers_are_equal(a, b):
    return a == b

def factorial_number(x):
    return math.factorial(x)

def factorial_squared(x):
    return factorial_number(x) ** 2

def double_value(x):
    return x * 2

def modulo(val, mod=1000000007):
    return val % mod

def case_equal(n, m):
    return modulo(double_value(factorial_squared(n)))

def case_diff_one(n, m):
    return modulo(factorial_number(n) * factorial_number(m))

def handle_cases(n, m):
    diff = compute_absolute_difference(n, m)
    if diff <= 1:
        if numbers_are_equal(n, m):
            result = case_equal(n, m)
        else:
            result = case_diff_one(n, m)
    else:
        result = 0
    print(result)

def main():
    n, m = read_input()
    handle_cases(n, m)

main()