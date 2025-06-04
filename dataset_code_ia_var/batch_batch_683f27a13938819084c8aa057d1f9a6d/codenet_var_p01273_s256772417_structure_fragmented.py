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

def input_list_int():
    return [int(x) for x in sys.stdin.readline().split()]

def input_list_int_minus1():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def input_list_float():
    return [float(x) for x in sys.stdin.readline().split()]

def input_list_str():
    return sys.stdin.readline().split()

def input_int():
    return int(sys.stdin.readline())

def input_float():
    return float(sys.stdin.readline())

def input_str():
    return input()

def print_flush(s):
    print(s, flush=True)

def read_n_and_m():
    return input_list_int()

def check_if_end(n, m):
    return n == 0 and m == 0

def read_edges(m):
    edges = []
    for _ in range(m):
        edges.append(input_list_int())
    return edges

def sort_edges(edges):
    edges.sort()
    return edges

def initialize_connected_set():
    return set([1])

def process_edges(edges, connected_set):
    for t, s, d in edges:
        if s in connected_set:
            connected_set.add(d)
    return connected_set

def calculate_connected_count(connected_set):
    return len(connected_set)

def append_result(rr, val):
    rr.append(val)

def result_to_str_list(rr):
    return list(map(str, rr))

def join_results(res_list):
    return '\n'.join(res_list)

def main_loop():
    rr = []
    while True:
        n, m = read_n_and_m()
        if check_if_end(n, m):
            break
        edges = read_edges(m)
        edges = sort_edges(edges)
        connected_set = initialize_connected_set()
        connected_set = process_edges(edges, connected_set)
        count = calculate_connected_count(connected_set)
        append_result(rr, count)
    return rr

def main():
    set_recursion_limit()
    inf = get_inf()
    eps = get_eps()
    mod = get_mod()
    rr = main_loop()
    res_list = result_to_str_list(rr)
    output_str = join_results(res_list)
    return output_str

print(main())