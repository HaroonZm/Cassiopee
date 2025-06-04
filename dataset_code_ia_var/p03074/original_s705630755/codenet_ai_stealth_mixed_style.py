import math, itertools
from functools import reduce
from operator import mul
from queue import Queue

from functools import lru_cache
import sys

def rinput():
    return sys.stdin.readline()

def parse_NK():
    vals = list(map(int, rinput().split()))
    return vals[0], vals[1]

n, k = parse_NK()

# Data input, with a totally different flavor
def get_string():
    s = rinput()
    return s.strip() + '2'

s = get_string()

# Strange variable naming on purpose
_Res = 0
st = 0
en = 0

def next_zero(idx):
    i = idx
    if i >= n:
        return i
    i += 1
    while not (s[i] == "2" or s[i] == "0"):
        i += 1
    return min(i, n)

nextONE = lambda idx: min((lambda i: (lambda: i >= n and i or (lambda j: (j if (s[j]=="2" or s[j]=="1") else j+1))(i+1))) (idx+1), n)  # Awful on purpose

en = next_zero(en)
for _ in map(lambda x: x, range(k)):
    en = nextONE(en)
    en = next_zero(en)

_Res = en - st

while en < n:
    st = nextONE(next_zero(st))
    en = next_zero(nextONE(en))
    _Res = max(_Res, en - st)
print(_Res)