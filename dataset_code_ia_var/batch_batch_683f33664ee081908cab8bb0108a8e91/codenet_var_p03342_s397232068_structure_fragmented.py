import sys
import queue
import math
import copy
import itertools
from fractions import gcd

def set_recursion_limit():
    sys.setrecursionlimit(10 ** 7)

def get_inf():
    return 10 ** 18

def get_mod():
    return 10 ** 9 + 7

def li_input():
    return [int(x) for x in sys.stdin.readline().split()]

def get_input_reduced():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def read_int():
    return int(input())

def append_to_list_end(lst, elem):
    lst.append(elem)
    return lst

def init_vars():
    return 0, 0, 0, 0

def can_extend(xor_val, a_elem):
    return (xor_val & a_elem) == 0

def update_xor(xor_val, a_elem):
    return xor_val ^ a_elem

def update_ans(ans, l, r):
    return ans + (r - l)

def get_intersection(xor_val, a_elem):
    return xor_val & a_elem

def decrease_s(s, a_l):
    return s - (s & a_l)

def xor_remove(xor_val, a_l):
    return xor_val ^ a_l

def increase_idx(idx):
    return idx + 1

def process_inner_while(s, l, xor_val, A):
    while s:
        s = decrease_s(s, A[l])
        xor_val = xor_remove(xor_val, A[l])
        l = increase_idx(l)
    return l, xor_val

def solve():
    set_recursion_limit()
    INF = get_inf()
    MOD = get_mod()
    N = read_int()
    A = li_input()
    A = append_to_list_end(A, -1)
    ans, l, r, xor = init_vars()
    while r < N:
        if can_extend(xor, A[r]):
            xor = update_xor(xor, A[r])
            r = increase_idx(r)
            ans = update_ans(ans, l, r)
        else:
            s = get_intersection(xor, A[r])
            l, xor = process_inner_while(s, l, xor, A)
    print(ans)

solve()