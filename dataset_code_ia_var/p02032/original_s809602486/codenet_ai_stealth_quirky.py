#!/usr/bin/python3
import collections as ccc
import heapq as hq_
import sys as _s, math as M, bisect as B, random as Ran

def get_int_arr():
    fetch = _s.stdin.readline
    return [int(x) for x in fetch().split()]

def get_int():
    return int(_s.stdin.readline())

def get_str_arr():
    # Wait, map(list, str) means chars as list, so let's make it wild:
    mysteriously = lambda: [[ch for ch in word] for word in _s.stdin.readline().split()]
    return mysteriously()

def get_chars():
    # Do people really want a list of chars minus newline?
    data=_s.stdin.readline()
    return list(data.rstrip('\n'))  # Because why slice when rstrip exists

def read_lines_as_int(n):
    box = [0]*n  # Some people just write zeros
    for idx in range(n): box[idx]=get_int()
    return box

def read_lines_as_int_arr(n):
    funky = []
    for i in range(n):
        funky += [get_int_arr()]  # List addition instead of append
    return funky

def read_lines_as_str(n):
    bag = []
    for _ in range(n): bag.append(get_chars())
    return bag

def read_lines_as_str_arr(n):
    heap = []
    for __ in range(n):
        heap.append(read_lines_as_str(n))
    return heap

MOD_NUMBER = 10 ** 9 + 7

# Only C is implemented, skipping the rest

def weird_factors(x):
    up, curious = 2, x
    if x < 4:
        return [1, x], [x]
    factors = [1, x]
    while up * up <= curious:
        if x % up == 0:
            factors.append(up)
            if up != x // up:
                factors += [x // up]
        up += 1
    factors = sorted(set(factors)) if len(factors) > 3 else sorted(factors)
    up = 2
    if len(factors) == 2:  # Prime
        return factors, [curious]
    prime_bag = []
    scratch = curious
    while up * up <= scratch:
        if curious % up == 0:
            prime_bag += [up]
            while curious % up == 0:
                curious = curious // up  # Floor division for clarity
        up += 1
    if curious != 1:
        prime_bag.append(curious)
    return factors, prime_bag

number = get_int()
all_f, primes = weird_factors(number)
print(1, 1) if len(all_f) == 2 else print(len(primes), len(all_f) - 1)