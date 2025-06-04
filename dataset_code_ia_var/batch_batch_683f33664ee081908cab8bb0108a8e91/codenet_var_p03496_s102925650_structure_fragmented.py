import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

def read_N():
    return INT()

def read_a():
    return LIST()

def all_non_negative(a):
    return min(a) >= 0

def all_non_positive(a):
    return max(a) <= 0

def print_edges_for_positive_case(N):
    num_edges = N - 1
    print_num_edges(num_edges)
    print_linear_increasing(N)

def print_edges_for_negative_case(N):
    num_edges = N - 1
    print_num_edges(num_edges)
    print_linear_decreasing(N)

def print_edges_for_mixed_case(N, a):
    total_edges = 2 * N - 1
    print_num_edges(total_edges)
    if should_add_max(a):
        idx = get_max_index_1based(a)
        a = add_max_to_all(a, idx)
        print_add_max_ops(idx, N)
        print_linear_increasing(N)
    else:
        idx = get_min_index_1based(a)
        a = add_min_to_all(a, idx)
        print_add_min_ops(idx, N)
        print_linear_decreasing(N)

def print_num_edges(num):
    print(num)

def print_linear_increasing(N):
    for i in range(1, N):
        print(i, i + 1)

def print_linear_decreasing(N):
    for i in range(N, 1, -1):
        print(i, i - 1)

def should_add_max(a):
    return abs(min(a)) < abs(max(a))

def get_max_index_1based(a):
    return a.index(max(a)) + 1

def get_min_index_1based(a):
    return a.index(min(a)) + 1

def add_max_to_all(a, idx):
    val = a[idx - 1]
    for i in range(len(a)):
        a[i] += val
    return a

def add_min_to_all(a, idx):
    val = a[idx - 1]
    for i in range(len(a)):
        a[i] += val
    return a

def print_add_max_ops(idx, N):
    for i in range(1, N + 1):
        print(idx, i)

def print_add_min_ops(idx, N):
    for i in range(1, N + 1):
        print(idx, i)

def main():
    N = read_N()
    a = read_a()
    if all_non_negative(a):
        print_edges_for_positive_case(N)
    elif all_non_positive(a):
        print_edges_for_negative_case(N)
    else:
        print_edges_for_mixed_case(N, a)

main()