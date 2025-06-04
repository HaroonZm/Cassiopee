import sys as _s
import itertools as _i

def _0(x): return x // 1
def _1(x): return x % 1

for __ in _s.stdin:
    try:
        a, b = (lambda z: (int(z[0]), int(z[1])))(__.split())
    except:
        break
    _p = a / float(b)
    _r = (a % b) * 10
    _Z = dict()
    _Z[_r] = 0
    _S = []
    for idx in _i.count(1):
        p2 = _r // b
        _r = (_r % b) * 10
        _S.append(str(p2))
        if not _r:
            print ''.join(_S)
            break
        if _r in _Z:
            print ''.join(_S)
            print ''.join([' ']*_Z[_r] + ['^']*(idx - _Z[_r]))
            break
        _Z[_r] = idx