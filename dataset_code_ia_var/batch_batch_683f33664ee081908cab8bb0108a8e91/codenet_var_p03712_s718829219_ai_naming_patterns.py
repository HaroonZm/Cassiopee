####################
# Standard Imports #
####################

import sys
_input_reader = sys.stdin.readline

import math
import bisect
from collections import defaultdict as _defaultdict
from collections import deque as _deque
from functools import lru_cache as _lru_cache

################
# Global Const #
################

CONST_MODULO = 10**9+7
CONST_INFINITY = float('inf')

#################
# Input Helpers #
#################

def read_int(): return int(_input_reader().strip())
def read_str(): return _input_reader().strip()
def read_int_list(): return list(map(int, _input_reader().split()))
def read_str_list(): return list(map(str, _input_reader().split()))
def read_int_lines(n): return [int(_input_reader()) for _ in range(n)]
def read_str_lines(n): return [read_str() for _ in range(n)]
def read_int_matrix(n): return [list(map(int, _input_reader().split())) for _ in range(n)]
def read_str_matrix(n): return [list(map(str, _input_reader().split())) for _ in range(n)]

##################
# Output Helpers #
##################

def print_yes(): print("Yes"); return
def print_no(): print("No"); return

#########################
# Modular Inverse Utils #
#########################

def modular_inverse(x): return pow(x, CONST_MODULO-2, CONST_MODULO)

###################
# Combinatorics   #
###################

_factorial_table = []
def factorial(n):
    if len(_factorial_table) > n:
        return _factorial_table[n]
    if len(_factorial_table) == 0:
        _factorial_table.append(1)
    while len(_factorial_table) <= n:
        _factorial_table.append(_factorial_table[-1] * len(_factorial_table) % CONST_MODULO)
    return _factorial_table[n]

_inv_factorial_table = []
def inverse_factorial(n):
    if len(_inv_factorial_table) > n:
        return _inv_factorial_table[n]
    if len(_inv_factorial_table) == 0:
        _inv_factorial_table.append(1)
    while len(_inv_factorial_table) <= n:
        _inv_factorial_table.append(_inv_factorial_table[-1] * pow(len(_inv_factorial_table), CONST_MODULO-2, CONST_MODULO) % CONST_MODULO)
    return _inv_factorial_table[n]

def comb(n, r):
    if n == r: return 1
    if n < r or r < 0: return 0
    result = 1
    result = result * factorial(n) % CONST_MODULO
    result = result * inverse_factorial(r) % CONST_MODULO
    result = result * inverse_factorial(n - r) % CONST_MODULO
    return result

##################
# Factorization  #
##################

def factorize(n):
    result = []
    temp = n
    for i in range(2, int((-(-n**0.5 // 1)))+1):
        if temp % i == 0:
            count = 0
            while temp % i == 0:
                count += 1
                temp //= i
            result.append([i, count])
    if temp != 1:
        result.append([temp, 1])
    if result == []:
        result.append([n, 1])
    return result

##################
# Divisor Utils  #
##################

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

##################
# LCM and GCD    #
##################

def compute_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def compute_lcm(a, b):
    return a * b // compute_gcd(a, b)

##################
# Bit Utilities  #
##################

def bit_count(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

############################
# Number Base Conversions  #
############################

def base10_to_baseN(x, n):
    if x // n:
        return base10_to_baseN(x // n, n) + [x % n]
    return [x % n]

def baseN_to_base10(x, n):
    xstr = str(x)
    return sum(int(xstr[-i]) * n ** i for i in range(len(xstr)))

#########################
# Integer Logarithm     #
#########################

def integer_log(value, base):
    count = 0
    while value >= base:
        value //= base
        count += 1
    return count

###############
# Main Logic  #
###############

main_h, main_w = read_int_list()

print("#" * (main_w + 2))
for _ in range(main_h):
    print("#" + read_str() + "#")
print("#" * (main_w + 2))