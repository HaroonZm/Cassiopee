import sys as _s
from operator import itemgetter as _ig
from math import ceil as _ceil, floor as _floor, sqrt as _sqrt
from fractions import gcd as _gcd
from copy import deepcopy as _cp
import heapq as _hq
from collections import Counter as _c, deque as _d
from functools import reduce as _r

_s.setrecursionlimit(2 * 10**5)
_input = lambda: _s.stdin.readline()
_ii = lambda: int(_input())
_mi = lambda: map(int, _input().split())
_lmi = lambda: list(map(int, _input().split()))
_li = lambda: list(_input().strip())
_debug = lambda *a, **k: (_s.stderr.write("debug: " + " ".join(map(str, a)) + k.get('end', '\n')) if not __debug__ else None)
_exit = lambda *a: (print(*a), _s.exit())

def main():
    AAA, BBB, CCC = _mi()
    f = lambda x, y: (x * y) % 2 == 0
    if all(map(lambda p: f(*p), ((AAA, BBB), (BBB, CCC), (CCC, AAA)))):
        print('Tem')
    else:
        print('Hom')

if __name__ == "__main__":
    main()