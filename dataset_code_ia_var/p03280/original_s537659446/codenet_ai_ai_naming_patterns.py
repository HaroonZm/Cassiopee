import math as mth
import sys as sys_mod
from bisect import bisect_left as bsct_lft, bisect_right as bsct_rgt
from collections import Counter as cnt_dict, defaultdict as dflt_dict, deque as dbl_ended_q
from copy import deepcopy as dcp
from functools import lru_cache as lru_cch
from heapq import heapify as hpify, heappop as hppop, heappush as hppush
from itertools import accumulate as accm, combinations as cmbs, permutations as prms

input_fn = sys_mod.stdin.readline
MOD_CONST = 10**9 + 7

read_str = lambda: input_fn().strip()
read_int = lambda: int(input_fn().strip())
read_ints = lambda: map(int, input_fn().split())
read_list = lambda: list(map(int, input_fn().split()))

val_a, val_b = read_ints()

print(val_a * val_b - val_a - val_b + 1)