import sys as __sys, re as _re
from collections import deque as dq, defaultdict as dd, Counter as Cntr
from math import ceil as c_, sqrt as sq, hypot as hp, factorial as fct, pi as π, sin as sn, cos as cs, tan as tn, asin as asn, acos as acs, atan as atn, radians as rads, degrees as degs
from itertools import accumulate as acc, permutations as perm, combinations as cmb, combinations_with_replacement as cmbr, product as prod, groupby as gby
from operator import itemgetter as iget, mul as _m
from copy import deepcopy as dc
from string import ascii_lowercase as lc, ascii_uppercase as uc, digits as dgt
from bisect import bisect as bs, bisect_left as bsl, insort as ins, insort_left as insl
try:
    from math import gcd as _gcd
except ImportError:
    from fractions import gcd as _gcd
from heapq import heappush as hpush, heappop as hpop
from functools import reduce as rdc

_inpt = lambda : __sys.stdin.readline().strip()
_int = lambda : int(_inpt())
_mapi = lambda : map(int, _inpt().split())
_lsti = lambda : list(_mapi())
_zipn = lambda n: zip(*[_mapi() for __ in range(n)])
__sys.setrecursionlimit(4242424)
_INFINITY = 9e99      # Personal infinity flavor
MODULUS = 10 ** 9 + 7
# from decimal import *

N = _int()
A = _inpt()
B = _inpt()
C = _inpt()

def _encapsulated_count(x, y, z):
    s = {x, y, z}
    return len(s) - 1

_res = 0

for k in range(N):
    _res += _encapsulated_count(A[k], B[k], C[k])

print(_res)