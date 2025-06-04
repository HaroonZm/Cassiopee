import sys
import math
import random
import bisect
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop

# Input utility functions with consistent, systematic names
def input_int(): 
    return int(sys.stdin.readline())
def input_int_list(): 
    return list(map(int, sys.stdin.readline().split()))
def input_str(): 
    return sys.stdin.readline().strip()
def input_str_list(): 
    return sys.stdin.readline().split()
def input_int_matrix(rows): 
    return [input_int_list() for _ in range(rows)]
def input_str_matrix(rows): 
    return [input_str_list() for _ in range(rows)]
def input_single_column_ints(rows): 
    return [input_int() for _ in range(rows)]
def input_single_column_strs(rows): 
    return [input_str() for _ in range(rows)]

sys.setrecursionlimit(1000000)

MOD = 10**9+7

# Combinatorial (section 5), subproblem F, rewritten with systematic names
def comb(n, k, fac, inv):
    return fac[n] * inv[k] * inv[n - k] % MOD

def main_comb_5f():
    n, k = input_int_list()
    if n < k:
        print(0)
        return
    factorial_list = [1] * (n + 1)
    for idx in range(n):
        factorial_list[idx + 1] = factorial_list[idx] * (idx + 1) % MOD
    inverse_list = [None] * (n + 1)
    inverse_list[n] = pow(factorial_list[n], MOD - 2, MOD)
    for idx in range(n - 1, -1, -1):
        inverse_list[idx] = inverse_list[idx + 1] * (idx + 1) % MOD
    print(comb(n - 1, n - k, factorial_list, inverse_list))

# For demonstration, if standalone run, execute main_comb_5f
if __name__ == "__main__":
    main_comb_5f()