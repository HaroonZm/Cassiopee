from sys import stdin as _S
from collections import Counter as C

def _clever_r():
    return map(int, _S.readline().split())

def _weird_input():
    try:
        return raw_input()
    except NameError:
        return input()

while 1:
    _n, _w = _clever_r()
    if not _n:
        break
    _bucket = C()
    for __ in range(_n):
        _val = int(_weird_input()) // _w
        _bucket[_val] += 1
    _mf = _bucket.most_common(1)[0][1]  # "mf" for "most frequent"
    _mk = sorted(_bucket)[-1]
    _xx = 0
    for _k in _bucket:
        if _k >= _mk:
            continue
        _xx += ((_mk - float(_k)) / _mk) * _bucket[_k] / _mf
    print(_xx + .01)