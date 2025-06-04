import math as mth
import string as strg
import itertools as it
import fractions as frct
import heapq as hpq
import collections as clct
import re as regex
import array as arr
import bisect as bsc
import sys as sysmod
import random as rnd
import time as tme
import copy as cpy
import functools as ftools

sysmod.setrecursionlimit(10**7)
CONST_INF = 10**20
CONST_EPS = 1.0 / 10**13
CONST_MOD = 10**9 + 7

DIRS_4 = [(-1,0), (0,1), (1,0), (0,-1)]
DIRS_8 = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

def read_int_list(): return [int(val) for val in sysmod.stdin.readline().split()]
def read_int_list_zero_based(): return [int(val)-1 for val in sysmod.stdin.readline().split()]
def read_float_list(): return [float(val) for val in sysmod.stdin.readline().split()]
def read_str_list(): return sysmod.stdin.readline().split()
def read_int(): return int(sysmod.stdin.readline())
def read_float(): return float(sysmod.stdin.readline())
def read_str(): return input()
def print_flush(msg): return print(msg, flush=True)

def main():
    result_list = []

    def get_concatenated_digits(num_n, num_m):
        n_val = num_n - 1
        num_start = 1
        digit_len = 1
        for k_idx in range(1, 10):
            count_in_segment = 10**(k_idx-1) * 9 * k_idx
            if n_val > count_in_segment:
                n_val -= count_in_segment
                num_start = 10 ** k_idx
                digit_len = k_idx + 1
            else:
                break
        num_start += n_val // digit_len
        n_val %= digit_len
        concat_str = ''
        for num_iter in range(num_start, num_start + 101):
            concat_str += str(num_iter)
        return concat_str[n_val:n_val+num_m]

    while True:
        vals = read_int_list()
        n_inp, m_inp = vals
        if n_inp == 0 and m_inp == 0:
            break
        result_list.append(get_concatenated_digits(n_inp, m_inp))

    return '\n'.join(map(str, result_list))

print(main())