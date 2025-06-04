import sys
sys.setrecursionlimit(10**6)
from math import floor, ceil, sqrt, factorial, log
from heapq import heappop, heappush, heappushpop
from collections import Counter, defaultdict, deque
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right
from copy import deepcopy
from operator import itemgetter
from fractions import gcd

mod = 10 ** 9 + 7
inf = float('inf')
ninf = -float('inf')

def input_int():
    return int(sys.stdin.readline().rstrip())

def input_ints():
    return map(int, sys.stdin.readline().rstrip().split())

def input_int_list():
    return list(input_ints())

def input_int_list_n(n):
    return [input_int() for _ in range(n)]

def input_int_2d_list(n):
    return [input_int_list() for _ in range(n)]

def input_str():
    return sys.stdin.readline().rstrip()

def input_strs():
    return sys.stdin.readline().rstrip().split()

def input_str_list():
    return list(input_strs())

def input_str_list_n(n):
    return [input_str() for _ in range(n)]

def input_str_2d_list(n):
    return [input_str_list() for _ in range(n)]

def parse_nm():
    n, m = input_ints()
    return n, m

def read_arr(n):
    return [read_pair() for _ in range(n)]

def read_pair():
    a, b = input_ints()
    return [a, b]

def read_mat(m):
    return [read_pair() for _ in range(m)]

def manhattan_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def find_nearest_index(i, j, mat):
    min_dist = float('inf')
    min_index = 1
    for idx, (c, d) in enumerate(mat, 1):
        d_ = manhattan_dist(i, j, c, d)
        if d_ < min_dist:
            min_dist = d_
            min_index = idx
    return min_index

def process_all(arr, mat):
    results = []
    for i, j in arr:
        index = find_nearest_index(i, j, mat)
        append_ans(results, index)
    return results

def append_ans(results, value):
    results.append(value)

def print_ans(ans):
    print(*ans)

def main():
    n, m = parse_nm()
    arr = read_arr(n)
    mat = read_mat(m)
    ans = process_all(arr, mat)
    print_ans(ans)

main()