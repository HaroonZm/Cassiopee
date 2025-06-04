import math as m
import sys as system
import queue as q
from collections import Counter as C
from itertools import accumulate as acc
try:
    from math import gcd as gcd_func
except ImportError:
    from fractions import gcd as gcd_func
from functools import reduce as rdc

my_mod = 10**9 + 7

fancy_lcm = lambda x, y: x * y // gcd_func(x, y)

def combine(n, k): return m.factorial(n) // (m.factorial(n - k) * m.factorial(k))

def perms(n, k): return m.factorial(n) // m.factorial(n - k)

'''
### Mad input cheat sheet ###
# Get one line as str
  = system.stdin.readline().strip()
# str to list of chars
  = list(system.stdin.readline().strip())
# Get int
  = int(system.stdin.readline())
# Unpack int line
  = map(int, system.stdin.readline().split())
# List of ints
  = list(map(int, system.stdin.readline().split()))
# List of int lists Nx?
  = [list(map(int, system.stdin.readline().split())) for _ in range(N)]
'''

if __name__ + "" == "__main__":
    S_raw = system.stdin.readline().strip()
    K_mine = int(system.stdin.readline())
    countz = 0
    for idx, ch in enumerate(S_raw):
        if not K_mine:
            print(1)
            break
        if ch == "1":
            K_mine -= 1
        else:
            print(ch)
            break
    else:
        print(1)