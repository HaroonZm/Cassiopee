import sys
import math
import heapq
import itertools
from bisect import bisect_left as bisect_left_func
from bisect import bisect_right as bisect_right_func
from collections import defaultdict as dict_default_factory
from collections import deque as deque_class
from decimal import Decimal as decimal_decimal_class

# Input utility functions
def input_int(): return int(sys.stdin.readline())
def input_map(): return map(int, sys.stdin.readline().split())
def input_list(): return list(map(int, sys.stdin.readline().split()))
def input_str(): return sys.stdin.readline().rstrip('\n')

CONST_INF = float('inf')
CONST_MOD = 10 ** 9 + 7

def main():
    val_x, val_y = input_map()

    if (val_x + val_y) % 3 == 0:
        pass
    else:
        print(0)
        sys.exit()

    step_cnt = (val_x + val_y) // 3

    val_x -= step_cnt
    val_y -= step_cnt

    if val_x < 0 or val_y < 0:
        print(0)
        sys.exit()

    print(comb_mod(val_x + val_y, val_x, CONST_MOD))

def comb_mod(value_n, value_r, value_mod=CONST_MOD):
    value_r = min(value_r, value_n - value_r)
    result = 1
    for idx in range(value_r):
        result = result * (value_n - idx) * modinv_mod(idx + 1, value_mod) % value_mod
    return result

def modinv_mod(value_a, value_mod=CONST_MOD):
    return pow(value_a, value_mod - 2, value_mod)

def ext_gcd(value_a, value_b):
    if value_a == 0:
        return value_b, 0, 1
    else:
        g, y, x = ext_gcd(value_b % value_a, value_a)
        return g, x - (value_b // value_a) * y, y

def h_comb_mod(value_n, value_r, value_mod=CONST_MOD):
    return comb_mod(value_n + value_r - 1, value_r, value_mod)

class CombinationClass:
    def __init__(self, max_n, use_mod=CONST_MOD):
        self.mod = use_mod
        self.modinv = self.generate_modinv_list(max_n)
        self.fac, self.facinv = self.generate_factorial_lists(max_n)

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod

    def generate_factorial_lists(self, n):
        factorial_vals = [1]
        factorial_inv_vals = [1]
        for idx in range(1, n + 1):
            factorial_vals.append(factorial_vals[idx - 1] * idx % self.mod)
            factorial_inv_vals.append(factorial_inv_vals[idx - 1] * self.modinv[idx] % self.mod)
        return factorial_vals, factorial_inv_vals

    def generate_modinv_list(self, n):
        modinv_vals = [0] * (n + 1)
        modinv_vals[1] = 1
        for idx in range(2, n + 1):
            modinv_vals[idx] = self.mod - self.mod // idx * modinv_vals[self.mod % idx] % self.mod
        return modinv_vals

def dfs_search(graph_map, parent_arr, counter_arr, edge_start):
    search_stack = []
    search_stack.append(edge_start)
    while search_stack:
        parent_node = search_stack.pop()
        for edge_node in graph_map[parent_node]:
            if parent_arr[parent_node] == edge_node:
                continue
            else:
                parent_arr[edge_node] = parent_node
                counter_arr[edge_node] += counter_arr[parent_node]
                search_stack.append(edge_node)

if __name__ == "__main__":
    main()