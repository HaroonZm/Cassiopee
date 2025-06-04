import math
from collections import deque
import itertools
import heapq
from fractions import Fraction
import copy
from functools import lru_cache
from collections import defaultdict
import pprint

MOD = 10 ** 9 + 7
INFI = 10 ** 10

def is_prime_step(n, k):
    return n % k == 0

def is_prime_range(n):
    return range(2, int(math.sqrt(n)) + 1)

def sosuhante(n):
    for k in is_prime_range(n):
        if is_prime_step(n, k):
            return False
    return True

def _fix_r(n, r):
    if n - r < r:
        r = n - r
    return r

def _special_cases_comb(n, r):
    if r == 0:
        return 1
    if r == 1:
        return n
    return None

def _build_numerator(n, r):
    return [n - r + k + 1 for k in range(r)]

def _build_denominator(r):
    return [k + 1 for k in range(r)]

def _fractional_reduction(p, n, r, numerator, denominator):
    pivot = denominator[p - 1]
    if pivot > 1:
        offset = (n - r) % p
        for k in range(p - 1, r, p):
            numerator[k - offset] /= pivot
            denominator[k] /= pivot

def _reduce_fractions(r, n, numerator, denominator):
    for p in range(2, r + 1):
        _fractional_reduction(p, n, r, numerator, denominator)

def _final_comb(r, numerator):
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result

def cmb(n, r):
    r = _fix_r(n, r)
    sc = _special_cases_comb(n, r)
    if sc is not None:
        return sc
    numerator = _build_numerator(n, r)
    denominator = _build_denominator(r)
    _reduce_fractions(r, n, numerator, denominator)
    return _final_comb(r, numerator)

def _num_digits(n):
    return len(str(n))

def kingaku(a, b, n):
    keta = _num_digits(n)
    return a * n + b * keta

def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default

def _pairwise_abs(a):
    c = [None] * (len(a) - 1)
    for i in range(1, len(a)):
        c[i - 1] = abs(a[i] - a[i - 1])
    return c

def _ret_base_cases(a):
    if len(a) == 1:
        return a[0]
    elif len(a) == 0:
        return 0
    return None

def ret(a):
    base_case = _ret_base_cases(a)
    if base_case is not None:
        return base_case
    c = _pairwise_abs(a)
    return ret(c)

def _soinsubunkai_loop_body(i, n, a):
    if n % i == 0 and i != 1:
        a.append(i)
        n = n // i
    return n

def _soinsubunkai_increment(i, n):
    if n % i != 0 or i == 1:
        i += 1
    return i

def soinsubunkai(n):
    a = []
    i = 1
    while i * i <= n:
        n_ = _soinsubunkai_loop_body(i, n, a)
        if n_ != n:
            n = n_
        i = _soinsubunkai_increment(i, n)
    nokori = [n]
    return a + nokori

def _divisor_body(n, i, lower_divisors, upper_divisors):
    if n % i == 0:
        lower_divisors.append(i)
        if i != n // i:
            upper_divisors.append(n // i)

def _divisor_loop(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        _divisor_body(n, i, lower_divisors, upper_divisors)
        i += 1
    return lower_divisors, upper_divisors

def make_divisors(n):
    lower_divisors, upper_divisors = _divisor_loop(n)
    return lower_divisors + upper_divisors[::-1]

def _read_input():
    return input()

def _parse_input(line):
    return map(int, line.split())

def _evaluate_condition(d, t, s):
    return t * s >= d

def _print_yes():
    print("Yes")

def _print_no():
    print("No")

def main_logic(d, t, s):
    if _evaluate_condition(d, t, s):
        _print_yes()
    else:
        _print_no()

def main():
    line = _read_input()
    d, t, s = _parse_input(line)
    main_logic(d, t, s)

if __name__ == "__main__":
    main()