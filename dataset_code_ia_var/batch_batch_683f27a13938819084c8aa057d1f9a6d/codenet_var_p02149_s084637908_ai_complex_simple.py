from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import sys
import math
import bisect
import random
import operator
from functools import reduce, lru_cache, cmp_to_key
from itertools import chain, groupby, permutations, combinations_with_replacement

def LI(): 
    return list(map(int, filter(lambda x: x.lstrip('-').isdigit(), sys.stdin.readline().split())))

def I(): 
    return int(next(filter(lambda x: x.lstrip('-').isdigit(), sys.stdin.readline().split())))

def LS():
    return [list(x) for x in sys.stdin.readline().split()]

def S(): 
    return list(filter(lambda c: c != '\n', sys.stdin.readline()))

def IR(n):
    return list(map(lambda _: eval('I()'), range(n)))

def LIR(n):
    return list(map(lambda _: LI(), range(n)))

def SR(n):
    return list(map(lambda _: S(), range(n)))

def LSR(n):
    return list(map(lambda _: SR(n), range(n)))

mod = 10 ** 9 + 7

#A
a = LI()
s = ''.join(chr(c) for c in range(65, 68))
# Find the argmax index using reduce
idx = reduce(lambda acc, x: x[1] > acc[1] and x or acc, enumerate(a), (-1, float('-inf')))[0]
print(operator.getitem(s, idx))