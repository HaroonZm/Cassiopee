import numpy as np
from copy import deepcopy
import math
import itertools

def read_input():
    return int(input())

def to_str(num):
    return str(num)

def str_len(s):
    return len(s)

def int2digit(num):
    s = to_str(num)
    return str_len(s)

def digits_list(digit):
    return [7, 5, 3], digit

def make_cartesian(lst, digit):
    return itertools.product(lst, repeat=digit)

def tuple_to_str(t):
    return ''.join(map(str, t))

def tuples_to_strs(tuples):
    return list(map(tuple_to_str, tuples))

def filter_contains(char, lst):
    return [s for s in lst if char in s]

def filter_int(lst, chars):
    tmp = lst
    for c in chars:
        tmp = filter_contains(c, tmp)
    return tmp

def list_map_int(lst):
    return list(map(int, lst))

def mk753_digit(digit):
    lst, d = digits_list(digit)
    lst_753_tuple = make_cartesian(lst, d)
    lst_753_str = tuples_to_strs(lst_753_tuple)
    lst_753_filtered = filter_int(lst_753_str, ['7', '5', '3'])
    lst_753 = list_map_int(lst_753_filtered)
    return lst_753

def accumulate_753_less_digit(digit):
    total = 0
    for k in range(digit):
        total += count_753_of_digit(k)
    return total

def count_753_of_digit(k):
    return len(mk753_digit(k))

def mk753_same_digit_list(digit):
    return mk753_digit(digit)

def filter_le(lst, N):
    return [x for x in lst if x <= N]

def main():
    N = read_input()
    digit = int2digit(N)
    ans = accumulate_753_less_digit(digit)
    lst_753_samedigit = mk753_same_digit_list(digit)
    lst_753_samedigit_smaller = filter_le(lst_753_samedigit, N)
    ans += len(lst_753_samedigit_smaller)
    print(ans)

main()