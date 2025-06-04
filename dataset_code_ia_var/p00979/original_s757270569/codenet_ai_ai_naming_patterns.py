import math as mth
import string as strg
import itertools as it
import fractions as frc
import heapq as hpq
import collections as col
import re as rgx
import array as ary
import bisect as bsc
import sys as sys_mod
import copy as cpy
import functools as fnt
import time as tme
import random as rnd

sys_mod.setrecursionlimit(10**7)
CONST_INF = 10**20
CONST_EPS = 1.0 / 10**10
CONST_MOD = 10**9 + 7
DIR4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIR8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def input_int_list():
    return list(map(int, sys_mod.stdin.readline().split()))

def input_list_of_int_lists():
    return [list(map(int, line.split())) for line in sys_mod.stdin.readlines()]

def input_zero_based_int_list():
    return [int(x) - 1 for x in sys_mod.stdin.readline().split()]

def input_float_list():
    return [float(x) for x in sys_mod.stdin.readline().split()]

def input_str_list():
    return sys_mod.stdin.readline().split()

def input_single_int():
    return int(sys_mod.stdin.readline())

def input_single_float():
    return float(sys_mod.stdin.readline())

def input_single_str():
    return input()

def print_flush_str(s):
    return print(s, flush=True)

def print_err_str(s):
    return print(str(s), file=sys_mod.stderr)

def join_array(arr, separator):
    return separator.join(map(str, arr))

def join_2d_array(arr_2d, outer_sep, inner_sep):
    return outer_sep.join(inner_sep.join(map(str, row)) for row in arr_2d)

def main():
    var_n = input_single_int()

    def recursive_func(val_n):
        if val_n < 4:
            return val_n
        return (val_n - 1) % 3 + recursive_func((val_n - 1) // 3 - 1) + 2

    return recursive_func(var_n)

print(main())