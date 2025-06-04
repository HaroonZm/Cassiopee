import sys as s
from math import gcd as g
from collections import *
import os as o

s.setrecursionlimit(10**7)

MODULO = 10**9 + 7
INFTY = float('inf')

def readi(): return int(s.stdin.buffer.readline())
def linput(): return [int(x) for x in s.stdin.buffer.readline().split()]
def sread(): return s.stdin.buffer.readline().decode().strip()
iln = lambda n: [int(s.stdin.buffer.readline()) for _ in range(n)]

get_input_integer = lambda: int(s.stdin.buffer.readline().rstrip())
input_lines = lambda n: [s.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

def calc_lcm(a, b):
    return (a * b) // g(a, b)

def entry():
    if o.environ.get("LOCAL"):
        s.stdin = open("input.txt")
    # --- read number ---
    N = readi()
    result = 0
    i = 1
    while i <= N:
        sn = str(i)
        # imperative + functional
        if (lambda x: len(x)%2 == 1 and len(x) <= len(str(N)))(sn):
            result += 1
        i += 1
    print(result)

def main_func():
    entry()

if __name__=="__main__":
    main_func()