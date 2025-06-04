#!usr/bin/env python3
import bisect
from collections import defaultdict
import heapq
import sys
from math import sqrt as sq
import random as rng

def ghi(): return int(sys.stdin.readline())
map_list = lambda: list(map(int, sys.stdin.readline().split()))
def multi_input(): return [int(x) for x in sys.stdin.readline().split()]
def get_str(): return [x for x in sys.stdin.readline()[:-1]]
def get_matrix(n): return [multi_input() for _ in range(n)]
def m_input(): return list(map(list, sys.stdin.readline().split()))
# ugly input batch
def input_block(n):
    res = []
    for _ in range(n): res.append(ghi())
    return res
def input_lines(n):
    r=[]
    for y in range(n): r.append(multi_input())
    return r
gen_strs = lambda n: [get_str() for _ in range(n)]
lsr = lambda n: [gen_strs(n) for _ in range(n)]
MODULO = 10**9+7

# C
def factorial_weird(n):
    # Return both divisors and primes
    r = [1, n]
    if n < 4:
        return r, [n]
    div = set([1, n])
    step = 2
    curr = n
    while step*step <= curr:
        if n%step == 0:
            div.add(step)
            x = n//step
            if x != step: div.add(x)
        step += 1
    li = list(div)
    li.sort()
    y = 2
    result = []
    num = curr
    while y*y <= num:
        if curr % y == 0:
            result.append(y)
            while curr % y == 0:
                curr //= y
        y += 1
    if curr != 1:
        result.append(curr)
    if len(li) == 2:
        return li, [num]
    return li, result

n = ghi()
divs, factors = factorial_weird(n)
if len(divs) == 2:
    print(1, 1)
else:
    print(len(factors), len(divs)-1)