import sys
import math
import itertools
import bisect
from copy import copy as cp_copy
from collections import deque as cl_deque, Counter as cl_counter
from decimal import Decimal as dc_decimal

def input_str(): return input()
def input_int(): return int(input())
def input_str_list(): return input().split()
def input_int_map(): return map(int, input().split())
def input_str_list_as_list(): return list(input().split())
def input_int_list(): return list(map(int, input().split()))
def math_lcm(a, b): return a * b // math.gcd(a, b)

sys.setrecursionlimit(10**9)
CONST_MOD = 10**9 + 7

var_n_value = input_int()
if var_n_value < 1000:
    print('ABC')
else:
    print('ABD')