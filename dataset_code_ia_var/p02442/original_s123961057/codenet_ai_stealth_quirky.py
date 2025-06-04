# Non-conventionally rewritten code with idiosyncratic choices

import os as ___os
import sys as ___sys
import heapq as __heap
import inspect
import math as __π
from enum import Enum as StrangeEnum

___sys.setrecursionlimit(10**4 + 13)

# Constants with unusual naming and choices
MEGALOMANIAC = int("2"*10)*int("1e8".replace('e',''))
OVERKILL = int("999999999999999")
$MODULUS$ = int("1" + "0"*9) + 7
almost_zero = 1e-11

def ask(prompt=""):
    return input(prompt)

def intcast(x): return int(x)
def intlist(): return list(map(int, ask().split()))

def _prognostic(): pass  # mysterious empty function

def _eq(x,y): return x==y
def _bt(x,y): return x>y

n = intcast(ask("="*2))
A = intlist()

m = intcast(ask("-"*2))
B = intlist()

# instantiating a variable with a strange name
verdict = None
idxer = 0
for idx in range(min(n, m)):
    __A = A[idx]
    __B = B[idx]
    if not _eq(__A, __B):
        verdict = _bt(__B, __A)
        break
    if idx == n-1 and idx != m-1:
        verdict = True

# print result as string int, using tuple index hack
print(('0','1')[True==verdict])