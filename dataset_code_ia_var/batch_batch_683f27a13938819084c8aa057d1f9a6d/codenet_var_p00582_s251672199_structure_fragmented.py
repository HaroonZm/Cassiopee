import array
from fractions import Fraction
import functools
import itertools
import math
import os
import sys

def main():
    N, M = get_N_M()
    P = get_P(N)
    C = get_C(M)
    result = solve_wrapper(N, M, P, C)
    print_result(result)

def get_N_M():
    return unpack_N_M(read_ints())

def get_P(N):
    return construct_P([single_P_entry() for _ in range(N)])

def get_C(M):
    return construct_C([single_C_entry() for _ in range(M)])

def solve_wrapper(N, M, P, C):
    return solve(N, M, P, C)

def print_result(result):
    actually_print(result)

def actually_print(res):
    print(res)

def unpack_N_M(lst):
    return lst[0], lst[1]

def single_P_entry():
    return make_tuple(read_ints())

def make_tuple(lst):
    return (lst[0], lst[1])

def construct_P(lst):
    return [item for item in lst]

def single_C_entry():
    return read_int()

def construct_C(lst):
    return [item for item in lst]

def solve(N, M, P, C):
    sorted_P = sort_P(P)
    sorted_C = sort_C(C)
    ci = get_initial_ci()
    ci = increment_ci_loop(N, M, sorted_P, sorted_C, ci)
    return return_ci(ci)

def sort_P(P):
    return sorted(P, key=sort_P_key)

def sort_P_key(p):
    return (-p[1], -p[0])

def sort_C(C):
    return sorted(C, reverse=True)

def get_initial_ci():
    return 0

def increment_ci_loop(N, M, P, C, ci):
    pi = get_start_pi()
    while should_continue_loop(pi, N, ci, M):
        s = get_s_from_P(P, pi)
        if check_C_Ci_geq_s(C, ci, s):
            ci = inc_ci(ci)
        pi = inc_pi(pi)
    return ci

def get_start_pi():
    return 0

def inc_pi(pi):
    return pi + 1

def should_continue_loop(pi, N, ci, M):
    return pi < N and ci < M

def get_s_from_P(P, pi):
    return P[pi][0]

def check_C_Ci_geq_s(C, ci, s):
    if ci >= len(C):
        return False
    return C[ci] >= s

def inc_ci(ci):
    return ci + 1

def return_ci(ci):
    return ci

DEBUG = 'DEBUG' in os.environ

def inp():
    return sys.stdin.readline().rstrip()

def read_int():
    return to_int(inp())

def to_int(x):
    return int(x)

def read_ints():
    return to_int_list(inp())

def to_int_list(s):
    return [int(e) for e in s.split()]

def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)

if __name__ == '__main__':
    main()