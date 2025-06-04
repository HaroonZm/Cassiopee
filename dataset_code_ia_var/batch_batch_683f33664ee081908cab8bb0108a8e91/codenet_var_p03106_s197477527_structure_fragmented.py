import sys

import numpy as np
import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right
from operator import itemgetter as ig
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
INF = float("INF")
mod = 10 ** 9 + 7

def wi():
    return list(map(int, sys.stdin.readline().split()))

def wip():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def ws():
    return sys.stdin.readline().split()

def si():
    return int(sys.stdin.readline())

def ss():
    return input()

def hi(n):
    return [si() for _ in range(n)]

def hs(n):
    return [ss() for _ in range(n)]

def s_list():
    return list(input())

def mi(n):
    return [wi() for _ in range(n)]

def mip(n):
    return [wip() for _ in range(n)]

def ms(n):
    return [ws() for _ in range(n)]

def num_grid(n):
    return [[int(i) for i in sys.stdin.readline().split()[0]] for _ in range(n)]

def grid(n):
    return [s_list() for _ in range(n)]

def make_divisors(n):
    divisors = []
    def iterate(i, n, divisors):
        if i > int(n ** 0.5):
            return
        if n % i == 0:
            add_divisor(i, n, divisors)
        iterate(i+1, n, divisors)
    def add_divisor(i, n, divisors):
        divisors.append(i)
        if i != n // i:
            divisors.append(n // i)
    iterate(1, n, divisors)
    return sorted_divisors(divisors)

def sorted_divisors(divisors):
    divisors.sort()
    return divisors

def input_split():
    return input().split()

def map_to_int(lst):
    return list(map(int, lst))

def get_divisor_lists(a, b):
    return make_divisors(a), make_divisors(b)

def common_elements(a_list, b_list):
    return [x for x in a_list if is_in_b(x, b_list)]

def is_in_b(val, b_list):
    return val in b_list

def reverse_list(lst):
    return lst[::-1]

def print_element(lst, k):
    print(lst[k-1])

def parse_input():
    values = input_split()
    return unpack_input(map_to_int(values))

def unpack_input(vals):
    return vals[0], vals[1], vals[2]

def main():
    a, b, k = parse_input()
    a_list, b_list = get_divisor_lists(a, b)
    ans = common_elements(a_list, b_list)
    ans = reverse_list(ans)
    print_element(ans, k)

if __name__ == '__main__':
    main()