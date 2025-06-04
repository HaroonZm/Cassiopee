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
    return 1.0 / 10**10

def get_mod():
    return 10**9 + 7

def get_dd():
    return [(0, -1), (1, 0), (0, 1), (-1, 0)]

def get_ddn():
    return [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

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

def read_input_N():
    return I()

def read_input_A(n):
    return [LI() for _ in range(n)]

def create_ddict_int():
    return collections.defaultdict(int)

def update_dict_for_point(d, x, y, w):
    for i in range(2):
        update_dict_for_i(d, x, y, w, i)

def update_dict_for_i(d, x, y, w, i):
    for j in range(2):
        update_dict_entry(d, x, y, w, i, j)

def update_dict_entry(d, x, y, w, i, j):
    key = (x + i, y + j)
    d[key] += w

def get_max_val_from_dict(d):
    vals = list(d.values())
    return get_max_from_list(vals)

def get_max_from_list(vals):
    return max(vals)

def format_result(r):
    return '{} / 1'.format(r)

def main():
    set_recursion_limit()
    n = read_input_N()
    a = read_input_A(n)
    d = create_ddict_int()
    for point in a:
        x, y, w = point
        update_dict_for_point(d, x, y, w)
    r = get_max_val_from_dict(d)
    result = format_result(r)
    return result

print(main())