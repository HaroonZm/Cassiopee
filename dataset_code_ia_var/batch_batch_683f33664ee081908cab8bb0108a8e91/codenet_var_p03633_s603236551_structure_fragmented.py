import sys
sys.setrecursionlimit(2147483647)
INF = float("inf")
MOD = 10 ** 9 + 7

def read_input():
    return int(input())

def import_gcd():
    from fractions import gcd
    return gcd

def initial_ans():
    return 1

def multiply(a, b):
    return a * b

def compute_gcd(gcd_func, a, b):
    return gcd_func(a, b)

def compute_lcm(a, b, gcd_func):
    g = compute_gcd(gcd_func, a, b)
    m = multiply(a, b)
    return m // g

def read_and_process(n, gcd_func):
    ans = initial_ans()
    for _ in range(n):
        t = read_input()
        ans = compute_lcm(ans, t, gcd_func)
    return ans

def output_result(result):
    print(result)

def resolve():
    n = read_input()
    gcd_func = import_gcd()
    result = read_and_process(n, gcd_func)
    output_result(result)

resolve()