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

def set_recursion():
    sys.setrecursionlimit(10**7)

def init_inf():
    return 10**20

def init_eps():
    return 1.0 / 10**10

def init_mod():
    return 998244353

def get_dd():
    return [(0,-1),(1,0),(0,1),(-1,0)]

def get_ddn():
    return [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

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

def calculate_nn(n):
    return n ** 2

def calculate_r(n):
    return n * (2 ** 0.5)

def iteration_range(n):
    return int(n) + 1

def calculate_kk(nn, i):
    return nn - i ** 2

def check_break(kk):
    return kk < 0

def calculate_k(kk):
    return kk ** 0.5

def calculate_tr(i, k):
    return i + k

def adjust_tr_for_k(tr, k):
    if k < 1:
        tr += 1 - k
    return tr

def update_r(r, tr):
    if r < tr:
        r = tr
    return r

def solve_main():
    n = F()
    nn = calculate_nn(n)
    r = calculate_r(n)
    for i in range(iteration_range(n)):
        kk = calculate_kk(nn, i)
        if check_break(kk):
            break
        k = calculate_k(kk)
        tr = calculate_tr(i, k)
        tr = adjust_tr_for_k(tr, k)
        r = update_r(r, tr)
    return r

def main():
    set_recursion()
    result = solve_main()
    return result

print(main())