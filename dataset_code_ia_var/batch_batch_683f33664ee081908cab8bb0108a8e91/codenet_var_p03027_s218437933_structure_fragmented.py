from sys import exit, setrecursionlimit, stderr, stdin
from functools import reduce
from itertools import *
from collections import defaultdict, Counter
from bisect import bisect
import functools

def set_large_recursion_limit():
    setrecursionlimit(10**7)

def fast_input():
    return stdin.readline().strip()

def fast_read():
    return int(fast_input())

def fast_reads():
    return [int(x) for x in fast_input().split()]

def get_modulus():
    return 10**6 + 3

def initialize_factorials(mod):
    fact = [1] * mod
    for i in range(1, mod):
        fact[i] = (fact[i-1] * i) % mod
    return fact

def initialize_inverse_factorials(mod, fact):
    invfact = [0] * mod
    invfact[-1] = compute_modular_inverse(fact[-1], mod)
    fill_inverse_factorials(mod, invfact)
    return invfact

def fill_inverse_factorials(mod, invfact):
    for i in range(mod-2, -1, -1):
        invfact[i] = invfact[i+1] * (i+1) % mod

def compute_modular_inverse(n, mod):
    return pow(n, mod-2, mod)

def get_inverse(n, mod):
    return compute_modular_inverse(n, mod)

def handle_zero_x_case():
    return 0

def handle_zero_d_case(x, n, mod):
    return pow(x, n, mod)

def compute_k(x, d, mod):
    return x * get_inverse(d, mod) % mod

def check_overflow_condition(n, k, mod):
    return n + k - 1 >= mod

def handle_overflow_case():
    return 0

def compute_answer(n, k, fact, invfact, d, mod):
    value1 = fact[n + k - 1]
    value2 = invfact[k-1]
    value3 = pow(d, n, mod)
    res = value1 * value2 % mod
    res = res * value3 % mod
    return res

def solve_single_query(x, d, n, fact, invfact, mod):
    if x == 0:
        return handle_zero_x_case()
    if d == 0:
        return handle_zero_d_case(x, n, mod)
    k = compute_k(x, d, mod)
    if check_overflow_condition(n, k, mod):
        return handle_overflow_case()
    return compute_answer(n, k, fact, invfact, d, mod)

def process_queries(q, fact, invfact, mod):
    for _ in range(q):
        x, d, n = fast_reads()
        ans = solve_single_query(x, d, n, fact, invfact, mod)
        print(ans)

def main():
    set_large_recursion_limit()
    mod = get_modulus()
    fact = initialize_factorials(mod)
    invfact = initialize_inverse_factorials(mod, fact)
    q = fast_read()
    process_queries(q, fact, invfact, mod)

main()