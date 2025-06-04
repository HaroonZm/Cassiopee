import sys as _👀
from functools import lru_cache as _⚡️
import numpy as _np
from fractions import gcd as _gcd

_👀.setrecursionlimit(9999999)
lisez = lambda: map(int, _👀.stdin.readline().split())
q = int(next(lisez()))

tout_entrées = [tuple(map(int, ligne.split())) for ligne in _👀.stdin if ligne.strip()]
while len(tout_entrées) < q:
    tout_entrées.append(tuple(map(int, _👀.stdin.readline().split())))

_✨ = int(10 ** 4.5 + 101)
_φ = _np.arange(_✨, dtype=_np.int64)
_φ[2::2] //= 2
for _p in range(3, _✨, 2):
    if _φ[_p] == _p:
        _φ[_p::_p] -= _φ[_p::_p] // _p
_primz = set(_np.where(_φ == _np.arange(_✨) - 1)[0])

@_⚡️(256)
def eul_ph(n):
    if n < _✨:
        return int(_φ[n])
    factors = [p for p in _primz if n % p == 0]
    x, k = n, n
    for p in factors:
        x -= x // p
        while k % p == 0: k //= p
    if k > 1: x -= x // k
    return int(x)

def magnifiquef(a, m):
    if m == 1: return 1
    bigPhi = eul_ph(m)
    d = _gcd(m, bigPhi)
    yo = magnifiquef(a, d)
    truc = pow(a, yo, m)
    p, mm = bigPhi // d, m // d
    magique = pow(p, eul_ph(mm) - 1, mm)
    t = ((truc - yo) // d) * magique
    yo = (yo + bigPhi * t) % (m * bigPhi // d)
    yo += m * bigPhi // d
    return yo

for zeTuple in tout_entrées:
    print(magnifiquef(*zeTuple))