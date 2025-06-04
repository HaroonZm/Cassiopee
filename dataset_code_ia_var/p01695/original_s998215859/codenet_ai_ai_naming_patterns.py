import math as m_mod
import string as str_mod
import itertools as iter_mod
import fractions as fr_mod
import heapq as hq_mod
import collections as coll_mod
import re as re_mod
import array as arr_mod
import bisect as bis_mod
import sys as sys_mod
import random as rnd_mod
import time as time_mod
import copy as cpy_mod
import functools as fct_mod

sys_mod.setrecursionlimit(10**7)
CONST_INF = 10**20
CONST_EPS = 1.0 / 10**10
CONST_MOD = 998244353

def read_int_list():
    return [int(val) for val in sys_mod.stdin.readline().split()]

def read_int_list_zero():
    return [int(val) - 1 for val in sys_mod.stdin.readline().split()]

def read_float_list():
    return [float(val) for val in sys_mod.stdin.readline().split()]

def read_str_list():
    return sys_mod.stdin.readline().split()

def read_int():
    return int(sys_mod.stdin.readline())

def read_float():
    return float(sys_mod.stdin.readline())

def read_str():
    return input()

def print_flush(output):
    return print(output, flush=True)

def main():
    results_list = []

    while True:
        input_n = read_int()
        if input_n == 0:
            break
        line_list = [read_str() for _ in range(input_n)] + ['']
        dot_count_list = [0] * (input_n + 1)
        for idx in range(1, input_n):
            curr_line = line_list[idx]
            dot_count_list[idx] = len(curr_line.split('.')) - 1
        char_matrix = [[ch for ch in line_str] for line_str in line_list[:input_n]]
        for idx_row in range(input_n):
            curr_dot_count = dot_count_list[idx_row]
            if curr_dot_count == 0:
                continue
            char_matrix[idx_row][curr_dot_count - 1] = '+'
            search_index = idx_row
            for idx_search in range(idx_row + 1, input_n):
                if dot_count_list[idx_search] < curr_dot_count:
                    break
                if dot_count_list[idx_search] == curr_dot_count:
                    search_index = idx_search
                    break
            for idx_vert in range(idx_row + 1, search_index):
                char_matrix[idx_vert][curr_dot_count - 1] = '|'
            for idx_space in range(curr_dot_count - 1):
                if char_matrix[idx_row][idx_space] == '.':
                    char_matrix[idx_row][idx_space] = ' '
        for out_row in char_matrix:
            results_list.append(''.join(out_row))

    return '\n'.join(map(str, results_list))

print(main())