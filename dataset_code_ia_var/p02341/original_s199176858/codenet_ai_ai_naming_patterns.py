import bisect as bisect_util
import collections as collections_util
import copy as copy_util
import heapq as heapq_util
import itertools as itertools_util
import math as math_util
import string as string_util
import sys as sys_util

input_fn = lambda: sys_util.stdin.readline().rstrip()
sys_util.setrecursionlimit(10**7)

CONST_INF = float('inf')
CONST_MOD = 10**9 + 7

def read_int():
    return int(input_fn())

def read_float():
    return float(input_fn())

def read_str():
    return input_fn()

def read_int_list():
    return [int(token) for token in input_fn().split()]

def read_int_list_zero_based():
    return [int(token) - 1 for token in input_fn().split()]

def read_float_list():
    return [float(token) for token in input_fn().split()]

def read_str_list():
    return input_fn().split()

def main():
    var_n, var_k = read_int_list()
    if var_n <= var_k:
        var_result = 1
    else:
        var_result = 0
    print(var_result)

if __name__ == '__main__':
    main()