import sys
import math
import bisect
from fractions import gcd
from itertools import count, permutations
from functools import lru_cache
from collections import deque, defaultdict
from pprint import pprint

INF = float('inf')

def set_recursion_limit():
    sys.setrecursionlimit(1000000000)

def read_int():
    return int(input())

def read_ints():
    return map(int, input().split())

def read_list_of_ints():
    return list(read_ints())

def read_matrix(h):
    return [list(map(int, read_list_of_ints())) for _ in range(h)]

def compute_gcd(a, b):
    return gcd(a, b)

def compute_lcm(a, b):
    return (a * b) // compute_gcd(a, b)

def read_main_input():
    return list(read_ints())

def initialize_ans(n):
    return [0] * n

def compute_min_distance(i, j, x, y):
    d1 = abs(j - i)
    d2 = abs(x - i) + 1 + abs(j - y)
    d3 = abs(y - i) + 1 + abs(j - x)
    return min(d1, d2, d3)

def increment_ans(ans, dist):
    ans[dist] += 1

def process_pairs(n, x, y, ans):
    def loop_i(i):
        def loop_j(j):
            dist = compute_min_distance(i, j, x, y)
            increment_ans(ans, dist)
        for j in range(i+1, n+1):
            loop_j(j)
    for i in range(1, n):
        loop_i(i)

def print_ans(ans):
    def print_entry(i, a):
        if i == 0:
            return
        print(a)
    for i, a in zip(range(len(ans)), ans):
        print_entry(i, a)

def main():
    set_recursion_limit()
    n, x, y = read_main_input()
    ans = initialize_ans(n)
    process_pairs(n, x, y, ans)
    print_ans(ans)

main()