######################
# library_imports    #
######################

import sys
input_stream = sys.stdin.readline

import math
import bisect
import heapq
from collections import defaultdict as coll_defaultdict
from collections import deque as coll_deque
from collections import Counter as coll_counter
from functools import lru_cache as fnc_lru_cache

######################
# global_constants   #
######################

CONST_MOD = 998244353
CONST_INF = float('inf')
CONST_AZ_LOWER = "abcdefghijklmnopqrstuvwxyz"

######################
# input_functions    #
######################

def input_int(): return int(input_stream().strip())
def input_str(): return input_stream().strip()
def input_int_list(): return list(map(int, input_stream().split()))
def input_str_list(): return list(map(str, input_stream().split()))
def input_int_lines(n): return [int(input_stream()) for _ in range(n)]
def input_str_lines(n): return [input_stream().strip() for _ in range(n)]
def input_nested_int_list(n): return [list(map(int, input_stream().split())) for _ in range(n)]
def input_nested_str_list(n): return [list(map(str, input_stream().split())) for _ in range(n)]

######################
# output_functions   #
######################

def output(val): print(val); return
def output_yes(): print("Yes"); return
def output_no(): print("No"); return
def exit_program(): exit()
def output_and_exit(val): print(val); exit()
def output_yes_and_exit(): print("Yes"); exit()
def output_no_and_exit(): print("No"); exit()

######################
# helper_functions   #
######################

def make_defaultdict(factory): return coll_defaultdict(factory)

def modular_inverse(n): return pow(n, CONST_MOD - 2, CONST_MOD)

_fact_cache = []
def factorial_mod(n):
    if len(_fact_cache) > n:
        return _fact_cache[n]
    if not _fact_cache:
        _fact_cache.append(1)
    while len(_fact_cache) <= n:
        _fact_cache.append(_fact_cache[-1] * len(_fact_cache) % CONST_MOD)
    return _fact_cache[n]

_inv_fact_cache = []
def inv_factorial_mod(n):
    if len(_inv_fact_cache) > n:
        return _inv_fact_cache[n]
    if not _inv_fact_cache:
        _inv_fact_cache.append(1)
    while len(_inv_fact_cache) <= n:
        _inv_fact_cache.append(_inv_fact_cache[-1] * pow(len(_inv_fact_cache), CONST_MOD - 2, CONST_MOD) % CONST_MOD)
    return _inv_fact_cache[n]

def comb_mod(n, r):
    if n == r:
        return 1
    if n < r or r < 0:
        return 0
    ret = factorial_mod(n)
    ret = ret * inv_factorial_mod(r) % CONST_MOD
    ret = ret * inv_factorial_mod(n - r) % CONST_MOD
    return ret

def prime_factorize(n):
    res = []
    t = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if t % i == 0:
            cnt = 0
            while t % i == 0:
                cnt += 1
                t //= i
            res.append([i, cnt])
    if t != 1:
        res.append([t, 1])
    if not res:
        res.append([n, 1])
    return res

def list_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def list_primes_up_to(N):
    max_val = int(math.sqrt(N))
    sieve_list = [i for i in range(2, N + 1)]
    res_primes = []
    while sieve_list and sieve_list[0] <= max_val:
        res_primes.append(sieve_list[0])
        tmp = sieve_list[0]
        sieve_list = [i for i in sieve_list if i % tmp != 0]
    res_primes.extend(sieve_list)
    return res_primes

def gcd_val(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm_val(a, b):
    return a * b // gcd_val(a, b)

def bit_count(n):
    cnt = 0
    while n:
        n &= n - 1
        cnt += 1
    return cnt

def base10_to_baseN(x, n):
    if x // n:
        return base10_to_baseN(x // n, n) + [x % n]
    return [x % n]

def baseN_to_base10(x, base):
    return sum(int(str(x)[-i-1]) * base ** i for i in range(len(str(x))))

def int_log_base(n, a):
    cnt = 0
    while n >= a:
        n //= a
        cnt += 1
    return cnt

######################
#     main_code      #
######################

in_str, in_k = input_str_list()
param_k = int(in_k)

block_list = []
cnt_1_total = 0
cnt_1_block = 0
for ch in in_str:
    if ch == "1":
        cnt_1_block += 1
        cnt_1_total += 1
    else:
        block_list.append(cnt_1_block)
        cnt_1_block = 0
block_list.append(cnt_1_block)
block_list = block_list[::-1]
block_cnt = len(block_list)
param_k = min(param_k, cnt_1_total)

dp_arr = [[[0 for _ in range(param_k + 1)] for _ in range(param_k + 1)] for _ in range(block_cnt)]
for idx_i in range(block_cnt):
    dp_arr[idx_i][0][0] = 1
for idx_k in range(min(block_list[0] + 1, param_k + 1)):
    dp_arr[0][idx_k][idx_k] = 1

for idx_i in range(1, block_cnt):
    for idx_k in range(param_k + 1):
        for idx_j in range(param_k + 1)[::-1]:
            if idx_j == param_k:
                dp_arr[idx_i][idx_k][idx_j] = dp_arr[idx_i - 1][idx_k][idx_j]
                dp_arr[idx_i][idx_k][idx_j] %= CONST_MOD
            else:
                dp_arr[idx_i][idx_k][idx_j] = dp_arr[idx_i - 1][idx_k][idx_j] + dp_arr[idx_i][idx_k][idx_j + 1]
                dp_arr[idx_i][idx_k][idx_j] %= CONST_MOD
    val_a = block_list[idx_i]
    if val_a:
        for idx_k in range(param_k):
            window = coll_deque([dp_arr[idx_i - 1][idx_k][0]])
            window_sum = dp_arr[idx_i - 1][idx_k][0]
            for idx_j in range(1, param_k + 1):
                if idx_k + idx_j > param_k: break
                dp_arr[idx_i][idx_k + idx_j][idx_j] += window_sum
                dp_arr[idx_i][idx_k + idx_j][idx_j] %= CONST_MOD
                window.append(dp_arr[idx_i - 1][idx_k + idx_j][idx_j])
                window_sum += dp_arr[idx_i - 1][idx_k + idx_j][idx_j]
                if len(window) > val_a:
                    window_sum -= window.popleft()
                window_sum %= CONST_MOD

ans_total = 0
for idx_k in range(param_k + 1):
    ans_total += dp_arr[-1][idx_k][0]
    ans_total %= CONST_MOD

print(ans_total)