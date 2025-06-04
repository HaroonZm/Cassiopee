#!/usr/bin/env python3
from collections import defaultdict as dict_default, deque as queue_deque
from heapq import heappush as heap_push, heappop as heap_pop
from bisect import bisect_left as bisect_left_func, bisect_right as bisect_right_func
import sys as sys_module, random as random_module, itertools as itertools_module, math as math_module
sys_module.setrecursionlimit(10**5)
input_func = sys_module.stdin.readline
math_sqrt = math_module.sqrt

def input_list_int(): return list(map(int, input_func().split()))
def input_list_float(): return list(map(float, input_func().split()))
def input_list_int_0idx(): return list(map(lambda x: int(x)-1, input_func().split()))
def input_single_int(): return int(input_func())
def input_single_float(): return float(input_func())
def input_list_str_lists(): return list(map(list, input_func().split()))
def input_single_str(): return input_func().rstrip()
def input_row_int(n_row): return [input_single_int() for _ in range(n_row)]
def input_row_list_int(n_row): return [input_list_int() for _ in range(n_row)]
def input_row_float(n_row): return [input_single_float() for _ in range(n_row)]
def input_row_list_float(n_row): return [input_list_int() for _ in range(n_row)]
def input_row_list_int_0idx(n_row): return [input_list_int_0idx() for _ in range(n_row)]
def input_row_str(n_row): return [input_single_str() for _ in range(n_row)]
def input_row_list_str_lists(n_row): return [input_list_str_lists() for _ in range(n_row)]

CONST_MOD = 1000000007
CONST_INF = 1e10
fact = [1] * 1010
ifact = [1] * 1010
bern_seq = [0] * 1010

def mod_add(val_x, val_y=0):
    return (val_x + val_y) % CONST_MOD

def mod_mul(val_x, val_y=1):
    return (val_x * val_y) % CONST_MOD

def mod_pow(val_x, val_y):
    return pow(val_x, val_y, CONST_MOD)

def mod_inv(val_x):
    return mod_pow(val_x, CONST_MOD - 2)

def bernoulli_number(idx):
    if idx > 0 and bern_seq[idx] == 0:
        bern_seq[idx] = mod_add(1, mod_mul(idx, bernoulli_number(idx - 1)))
    return bern_seq[idx]

def solve_problem():
    for idx in range(1, 1010):
        fact[idx] = fact[idx - 1] * idx
    for idx in range(1010):
        ifact[idx] = mod_inv(fact[idx])
    current_num = 1
    dp_arr = [[[0] * 1010 for _ in range(2)] for i_depth in range(1010)]
    dp_count = [0] * 1010
    flag_arr = [False] * 1010
    var_n = input_single_int()
    str_s = input_single_str()
    if var_n == 1 and str_s == "-":
        print("{} 0 {}".format((CONST_MOD + 1) // 2, (CONST_MOD + 1) // 2))
        return
    ptr_q = 0
    ptr_r = var_n
    var_n = -1
    if str_s[ptr_q] == "-":
        ptr_q += 1
    if str_s[ptr_q] == "-":
        ptr_q += 1
        var_n += 1
        current_num += 1
    if str_s[ptr_q] == "-":
        print("0 0 0")
        return
    for idx in range(ptr_q, ptr_r):
        if str_s[idx] == "X":
            if current_num == 0:
                print("0 0 0")
                return
            if var_n >= 0:
                flag_arr[var_n] = current_num - 1
            var_n += 1
            current_num = 0
        else:
            if current_num > 1:
                print("0 0 0")
                return
            current_num += 1
    if current_num == 2:
        flag_arr[var_n] = 1
        var_n += 1
    dp_count[0] = 1
    for idx in range(var_n):
        if flag_arr[idx]:
            for st in range(2):
                for t in range(2 * var_n + 2):
                    inv_val = mod_inv(t * t + 3 * t + 2)
                    dp_arr[idx + 1][st][0] = mod_add(dp_arr[idx + 1][st][0], mod_mul(dp_arr[idx][st][t], inv_val))
                    dp_arr[idx + 1][st][1] = mod_add(dp_arr[idx + 1][st][1], mod_mul(dp_arr[idx][st][t], CONST_MOD - inv_val))
            dp_arr[idx + 1][1][0] = mod_add(dp_arr[idx + 1][1][0], dp_count[idx])
            dp_arr[idx + 1][1][1] = mod_add(dp_arr[idx + 1][1][1], CONST_MOD - dp_count[idx])
        else:
            for st in range(2):
                for t in range(2 * var_n + 2):
                    inv_val = mod_inv(t + 1)
                    dp_arr[idx + 1][st][0] = mod_add(dp_arr[idx + 1][st][0], mod_mul(dp_arr[idx][st][t], inv_val))
                    dp_arr[idx + 1][st][1] = mod_add(dp_arr[idx + 1][st][1], mod_mul(dp_arr[idx][st][t], CONST_MOD - inv_val))
                    dp_arr[idx + 1][st][t + 2] = mod_add(dp_arr[idx + 1][st][t + 2], mod_mul(dp_arr[idx][st][t], mod_inv(t * t + 3 * t + 2)))
            dp_arr[idx + 1][1][1] = mod_add(dp_arr[idx + 1][1][1], dp_count[idx])
            dp_arr[idx + 1][1][0] = mod_add(dp_arr[idx + 1][1][0], CONST_MOD - dp_count[idx])
            dp_count[idx + 1] = mod_add(dp_count[idx + 1], dp_count[idx])
    ans_list = [0] * 3
    for st in range(2):
        for t in range(2 * var_n + 2):
            ans_list[st] = mod_add(ans_list[st], mod_mul(dp_arr[var_n][st][t], fact[t]))
            ans_list[st + 1] = mod_add(ans_list[st + 1], mod_mul(dp_arr[var_n][st][t], CONST_MOD - mod_add(fact[t], bernoulli_number(t))))
    tmp_val = (CONST_MOD + 1) // 2
    ans_list[0] = mod_add(ans_list[0], mod_mul(dp_count[var_n], tmp_val))
    ans_list[2] = mod_add(ans_list[2], mod_mul(dp_count[var_n], CONST_MOD - tmp_val))
    print("{} {} {}".format(ans_list[0], ans_list[1], ans_list[2]))
    return

if __name__ == '__main__':
    solve_problem()