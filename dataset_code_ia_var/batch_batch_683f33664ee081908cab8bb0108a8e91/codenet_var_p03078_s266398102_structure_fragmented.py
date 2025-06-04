import itertools
import sys
import math
from functools import lru_cache
from queue import Queue
from operator import mul
from functools import reduce

def read_input_line():
    return sys.stdin.readline()

def parse_ints_from_input():
    return list(map(int, read_input_line().split()))

def parse_list():
    return list(map(int, read_input_line().split()))

def parse_and_sort_list():
    lst = parse_list()
    lst.sort(reverse=True)
    return lst

def gather_inputs():
    x, y, z, kk = parse_ints_from_input()
    a = parse_and_sort_list()
    b = parse_and_sort_list()
    c = parse_and_sort_list()
    return x, y, z, kk, a, b, c

def should_break_i_j(i, j, kk):
    return i * j > kk

def should_break_i_j_k(i, j, k, kk):
    return i * j * k > kk

def sum_combinations(a, b, c, kk):
    ll = []
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if should_break_i_j(i, j, kk):
                break
            for k in range(len(c)):
                if should_break_i_j_k(i, j, k, kk):
                    break
                ll.append(compute_sum(a, b, c, i, j, k))
    return ll

def compute_sum(a, b, c, i, j, k):
    return a[i] + b[j] + c[k]

def sort_list_desc(lst):
    lst.sort(reverse=True)
    return lst

def print_top_k_elements(lst, k):
    for i in range(k):
        print(lst[i])

def main():
    x, y, z, kk, a, b, c = gather_inputs()
    ll = sum_combinations(a, b, c, kk)
    ll = sort_list_desc(ll)
    print_top_k_elements(ll, kk)

if __name__ == "__main__":
    main()