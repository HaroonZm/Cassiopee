import bisect
import copy
import heapq
import math
import sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

def custom_input():
    return sys.stdin.readline()[:-1]

def ruiseki(lst):
    return [0] + list(accumulate(lst))

def celi(a, b):
    return -(-a // b)

def set_recursion():
    sys.setrecursionlimit(5000000)

def get_mod():
    return pow(10, 9) + 7

def generate_alphabet():
    return [chr(ord('a') + i) for i in range(26)]

def get_directions():
    return [[1, 0], [0, 1], [-1, 0], [0, -1]]

def read_n():
    return int(custom_input())

def read_a():
    return list(map(int, custom_input().split()))

def init_ans():
    return 0

def init_l():
    return 0

def init_r():
    return 0

def init_cnt():
    return 0

def init_xor():
    return 0

def process_element(i, l, r, cnt, xor, a, n):
    l = i
    if is_l_eq_r(l, r):
        cnt, xor, r = add_element(cnt, xor, a[i], r)
    return l, r, cnt, xor

def is_l_eq_r(l, r):
    return l == r

def add_element(cnt, xor, ai, r):
    cnt_updated = cnt + ai
    xor_updated = xor + ai
    r_updated = r + 1
    return cnt_updated, xor_updated, r_updated

def can_extend(r, n):
    return r + 1 <= n

def can_extend_while(xor, cnt, a, r):
    return xor ^ a[r] == cnt + a[r]

def extend_window(xor, cnt, ai):
    xor_updated = xor ^ ai
    cnt_updated = cnt + ai
    return xor_updated, cnt_updated

def remove_element(cnt, xor, ai):
    cnt_updated = cnt - ai
    xor_updated = xor - ai
    return cnt_updated, xor_updated

def update_ans(ans, r, l):
    return ans + (r - l)

def main():
    set_recursion()
    mod = get_mod()
    al = generate_alphabet()
    direction = get_directions()
    n = read_n()
    a = read_a()
    ans = init_ans()
    l = init_l()
    r = init_r()
    cnt = init_cnt()
    xor = init_xor()
    for i in range(n):
        l, r, cnt, xor = process_element(i, l, r, cnt, xor, a, n)
        while can_extend(r, n) and can_extend_while(xor, cnt, a, r):
            xor, cnt = extend_window(xor, cnt, a[r])
            r += 1
        cnt, xor = remove_element(cnt, xor, a[i])
        ans = update_ans(ans, r, l)
    print(ans)

main()