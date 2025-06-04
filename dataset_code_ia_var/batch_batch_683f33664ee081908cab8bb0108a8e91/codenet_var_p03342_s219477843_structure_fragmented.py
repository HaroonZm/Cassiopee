import sys
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter

input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = float("inf")
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)

def read_n():
    return getN()

def read_list():
    return getList()

def initial_xo():
    return 0

def initial_su():
    return 0

def initial_ans():
    return 0

def initial_l():
    return 0

def initial_r():
    return 0

def initial_forward():
    return True

def r_equals_n(r, n):
    return r == n

def print_ans_and_return(ans):
    print(ans)
    return

def xo_su_equal(xo, su):
    return xo == su

def increase_ans_segment(ans, l, r):
    return ans + r - l + 1

def increase_ans_segment_no_eq(ans, l, r):
    return ans + r - l

def xor_val(a, b):
    return a ^ b

def add_val(a, b):
    return a + b

def sub_val(a, b):
    return a - b

def increase_r(r):
    return r + 1

def increase_l(l):
    return l + 1

def process_forward(xo, su, ans, l, r, lis):
    xo = xor_val(xo, lis[r])
    su = add_val(su, lis[r])
    if xo_su_equal(xo, su):
        ans = increase_ans_segment(ans, l, r)
        r = increase_r(r)
        return xo, su, ans, l, r, True
    else:
        return xo, su, ans, l, r, False

def process_backward(xo, su, ans, l, r, lis):
    xo = xor_val(xo, lis[l])
    su = sub_val(su, lis[l])
    if xo_su_equal(xo, su):
        ans = increase_ans_segment_no_eq(ans, l, r)
        r = increase_r(r)
        l = increase_l(l)
        return xo, su, ans, l, r, True
    else:
        l = increase_l(l)
        return xo, su, ans, l, r, False

def solve_single_case():
    n = read_n()
    lis = read_list()
    xo = initial_xo()
    su = initial_su()
    ans = initial_ans()
    l = initial_l()
    r = initial_r()
    forward = initial_forward()
    while True:
        if r_equals_n(r, n):
            print_ans_and_return(ans)
            return
        if forward:
            xo, su, ans, l, r, forward = process_forward(xo, su, ans, l, r, lis)
        else:
            xo, su, ans, l, r, forward = process_backward(xo, su, ans, l, r, lis)

def main_loop():
    n = read_n()
    for _ in range(n):
        solve_single_case()
    return

if __name__ == "__main__":
    solve_single_case()