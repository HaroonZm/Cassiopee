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

def get_input_string():
    return S()

def get_length(s):
    return len(s)

def get_defaultdict_int():
    return collections.defaultdict(int)

def create_memo_dict():
    return {'': True}

def is_in_memo(s, m):
    return s in m

def get_first(s):
    return s[0]

def get_last(s):
    return s[-1]

def set_memo_false(s, m):
    m[s] = False

def set_memo_true(s, m):
    m[s] = True

def update_memo(s, value, m):
    m[s] = value

def check_substrings(s, m):
    l = get_length(s)
    for i in range(1, l-1):
        if s[i] != 'e':
            continue
        if eval_f(s[1:i], m) and eval_f(s[i+1:-1], m):
            set_memo_true(s, m)
            return True
    set_memo_false(s, m)
    return False

def eval_f(s, m):
    if is_in_memo(s, m):
        return m[s]
    if get_first(s) != 'm' or get_last(s) != 'w':
        set_memo_false(s, m)
        return False
    return check_substrings(s, m)

def get_result(s, m):
    if eval_f(s, m):
        return 'Cat'
    return 'Rabbit'

def main():
    set_recursion_limit()
    inf = get_inf()
    eps = get_eps()
    mod = get_mod()
    dd = get_dd()
    ddn = get_ddn()
    s = get_input_string()
    l = get_length(s)
    d = get_defaultdict_int()
    m = create_memo_dict()
    result = get_result(s, m)
    return result

print(main())