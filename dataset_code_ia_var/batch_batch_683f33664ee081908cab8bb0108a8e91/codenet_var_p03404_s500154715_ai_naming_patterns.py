############################
# Importing Standard Libs  #
############################

import sys
sys_input = sys.stdin.readline

import math
import bisect as bisect_lib
import heapq as heapq_lib
from collections import defaultdict as collections_defaultdict
from collections import deque as collections_deque
from collections import Counter as collections_Counter
from functools import lru_cache as functools_lru_cache

############################
# Constant Declarations    #
############################

CONST_MODULO = 10**9 + 7
CONST_INF = float('inf')
CONST_ALPHA_LOWER = "abcdefghijklmnopqrstuvwxyz"

############################
# Input Utility Functions  #
############################

def input_int(): return int(sys_input().strip())
def input_str(): return sys_input().strip()
def input_int_list(): return list(map(int, sys_input().split()))
def input_str_list(): return list(map(str, sys_input().split()))
def input_n_ints(n): return [int(sys_input()) for _ in range(n)]
def input_n_strs(n): return [sys_input().strip() for _ in range(n)]
def input_n_int_lists(n): return [list(map(int, sys_input().split())) for _ in range(n)]
def input_n_str_lists(n): return [list(map(str, sys_input().split())) for _ in range(n)]

############################
# Output Utility Functions #
############################

def print_arg(arg): print(arg); return
def print_yes(): print("Yes"); return
def print_no(): print("No"); return
def halt(): exit()
def print_arg_and_halt(arg): print(arg); exit()
def print_yes_and_halt(): print("Yes"); exit()
def print_no_and_halt(): print("No"); exit()

############################
# Utility Abbreviations    #
############################

def defaultdict_factory(factory_func): return collections_defaultdict(factory_func)

############################
# Inverse Modular Power    #
############################

def modular_inverse(n): return pow(n, CONST_MODULO-2, CONST_MODULO)

############################
# Precomputed Factorials   #
############################

factorial_list = []
def precompute_factorial(n):
    if len(factorial_list) > n:
        return factorial_list[n]
    if len(factorial_list) == 0:
        factorial_list.append(1)
    while len(factorial_list) <= n:
        factorial_list.append(factorial_list[-1] * len(factorial_list) % CONST_MODULO)
    return factorial_list[n]

inverse_factorial_list = []
def precompute_inverse_factorial(n):
    if len(inverse_factorial_list) > n:
        return inverse_factorial_list[n]
    if len(inverse_factorial_list) == 0:
        inverse_factorial_list.append(1)
    while len(inverse_factorial_list) <= n:
        inverse_factorial_list.append(
            inverse_factorial_list[-1] * pow(len(inverse_factorial_list), CONST_MODULO - 2, CONST_MODULO) % CONST_MODULO
        )
    return inverse_factorial_list[n]

def combination_nCr(n, r):
    if n == r:
        return 1
    if n < r or r < 0:
        return 0
    result = 1
    result = result * precompute_factorial(n) % CONST_MODULO
    result = result * precompute_inverse_factorial(r) % CONST_MODULO
    result = result * precompute_inverse_factorial(n - r) % CONST_MODULO
    return result

############################
# Prime Factorization      #
############################

def get_prime_factors(n):
    result = []
    temp_n = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp_n % i == 0:
            count = 0
            while temp_n % i == 0:
                count += 1
                temp_n //= i
            result.append([i, count])
    if temp_n != 1:
        result.append([temp_n, 1])
    if not result:
        result.append([n, 1])
    return result

############################
# All Divisors Generator   #
############################

def get_all_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

############################
# Prime Sieve Generator    #
############################

def generate_primes_up_to(max_n):
    max_root = int(math.sqrt(max_n))
    search_list = [i for i in range(2, max_n + 1)]
    primes = []
    while search_list and search_list[0] <= max_root:
        current = search_list[0]
        primes.append(current)
        search_list = [i for i in search_list if i % current != 0]
    primes.extend(search_list)
    return primes

############################
# GCD / LCM Functions      #
############################

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_lcm(a, b):
    return a * b // get_gcd(a, b)

############################
# Bit Operations           #
############################

def count_number_of_bits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

############################
# Base Conversion          #
############################

def convert_base10_to_baseN(val, base):
    if val // base:
        return convert_base10_to_baseN(val // base, base) + [val % base]
    return [val % base]

def convert_baseN_to_base10(val, base):
    val_str = str(val)
    return sum(int(val_str[-i - 1]) * base ** i for i in range(len(val_str)))

def convert_base10_to_baseN_no_zero(val, base):
    val -= 1
    if val // base:
        return convert_base10_to_baseN_no_zero(val // base, base) + [val % base]
    return [val % base]

############################
# Integer Logarithm        #
############################

def integer_logarithm(n, base):
    count = 0
    while n >= base:
        n //= base
        count += 1
    return count

############################
# Main Algorithm Section   #
############################

input_A, input_B = input_int_list()
print(100, 100)

main_grid_list_A = ['#'] * (25 * 50 - (input_A - 1)) + ['.'] * (input_A - 1)
main_grid_list_B = ['#'] * (input_B - 1) + ['.'] * (25 * 50 - (input_B - 1))

for row_idx_upper in range(25):
    for col_idx_upper in range(50):
        print(main_grid_list_A.pop(), end="")
        if col_idx_upper == 49:
            print("#")
        else:
            print("#", end="")
    print("#" * 100)
for row_idx_lower in range(25):
    print("." * 100)
    for col_idx_lower in range(50):
        print(main_grid_list_B.pop(), end="")
        if col_idx_lower == 49:
            print(".")
        else:
            print(".", end="")