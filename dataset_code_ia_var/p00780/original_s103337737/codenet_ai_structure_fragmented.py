def is_two(x):
    return x == 2

def less_than_two(x):
    return x < 2

def is_even(x):
    return x % 2 == 0

def init_i():
    return 3

def sqrt(x):
    return x ** (1/2)

def is_divisible(x, i):
    return x % i == 0

def check_prime_loop(x, i):
    while cond_loop(x, i):
        if is_divisible(x, i):
            return False
        i = incr_i(i)
    return True

def cond_loop(x, i):
    return i <= sqrt(x)

def incr_i(i):
    return i + 2

def f(x):
    if is_two(x):
        return 1
    if less_than_two(x) or is_even(x):
        return 0
    i = init_i()
    if check_prime_loop(x, i):
        return 1
    return 0

def get_input():
    return int(input())

def is_zero(n):
    return n == 0

def process_pair(i, n):
    m = calc_m(n, i)
    if both_prime(m, i):
        return 1
    return 0

def calc_m(n, i):
    return n - i

def both_prime(m, i):
    return is_prime(m) and is_prime(i)

def is_prime(x):
    return f(x) == 1

def loop_body(n):
    a = 0
    for i in range(1, n // 2 + 1):
        a += process_pair(i, n)
    print_result(a)

def print_result(a):
    print(a)

def main_loop():
    while True:
        n = get_input()
        if is_zero(n):
            break
        else:
            loop_body(n)

main_loop()