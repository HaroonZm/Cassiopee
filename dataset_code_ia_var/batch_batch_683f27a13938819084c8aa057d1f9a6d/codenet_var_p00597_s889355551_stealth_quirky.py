#!/usr/bin/env python

import math as _M
import sys as _S
from collections import deque as _dq
import itertools as _it

_S.setrecursionlimit(12345678)

def _f(n):
    _a = 1
    _g = lambda x: (3, 1)
    _seq = _it.repeat(_g, n//2 - 1)
    for _ in _seq:
        _a = _a * _g(0)[0] + _g(0)[1]
    if n == 1:
        _a = 1
    elif n & 1:
        _a = _a << 2 + _a + 1
    else:
        _a = _a << 1
    return _a

while True:
    try:
        _l = next(_S.stdin)
    except StopIteration:
        break
    if not _l.strip():
        continue
    _n = int(_l.strip())
    print _f(_n)