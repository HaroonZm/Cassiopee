import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import functools

def set_recursion_limit():
    sys.setrecursionlimit(10**7)

def get_inf():
    return 10**20

def get_eps():
    return 1.0 / 10**13

def get_mod():
    return 10**9+7

def get_dd():
    return [(-1,0),(0,1),(1,0),(0,-1)]

def get_ddn():
    return [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    return sys.stdin.readline().split()

def I():
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def S():
    return input()

def pf(s):
    return print(s, flush=True)

def init_dp(a0, inf):
    size = a0*2
    dp = [inf] * size
    fill_dp_initial_values(dp, a0)
    return dp

def fill_dp_initial_values(dp, a0):
    for i in range(a0//2, a0*2):
        dp[i] = calc_initial_value(i, a0)

def calc_initial_value(i, a0):
    return abs(i - a0) / a0

def create_ndp(a1, inf):
    nn = a1 * 2
    return [inf] * nn

def should_continue_dp(dp, j, inf):
    return dp[j] == inf

def update_ndp(ndp, k, u):
    if ndp[k] > u:
        ndp[k] = u

def get_u(a1, k):
    return abs(a1 - k) / a1

def maximize_u(u, t):
    if u < t:
        u = t
    return u

def process_inner_loops(j, nn, dp, a1, ndp):
    if should_continue_dp(dp, j, get_inf()):
        return
    t = dp[j]
    for k in range(j, nn, j):
        u = get_u(a1, k)
        u = maximize_u(u, t)
        update_ndp(ndp, k, u)

def iterate_a(a, n, dp, inf):
    for i in range(n-1):
        a1 = a[i+1]
        ndp = create_ndp(a1, inf)
        nn = a1 * 2
        for j in range(1, len(dp)):
            process_inner_loops(j, nn, dp, a1, ndp)
        dp = ndp
    return dp

def format_output(dp):
    return '{:0.9f}'.format(min(dp))

def process_f(n, inf):
    a = LI()
    dp = init_dp(a[0], inf)
    dp = iterate_a(a, n, dp, inf)
    return format_output(dp)

def is_end(n):
    return n == 0

def main():
    set_recursion_limit()
    inf = get_inf()
    rr = []
    while True:
        n = I()
        if is_end(n):
            break
        rr.append(process_f(n, inf))
        break
    return '\n'.join(map(str, rr))

print(main())