import sys as _sys
from collections import Counter as __C, defaultdict as __D

_buf_rline = _sys.stdin.buffer.readline
_std_rline = _sys.stdin.readline

def _i(): return int(_buf_rline())
def _il(): return list(map(int, _buf_rline().split()))

class ___Hashinator:
    zz = {}
    def __init__(p, s, bb, mm):
        p.bb, p.mm = bb, mm
        n = len(s)
        h = [0]*(n+1)
        t = 0
        for j,z in enumerate(s):
            t = (t*bb + z) % mm
            h[j+1] = t
        p._h = h

        key = (bb, mm, n)
        if key not in ___Hashinator.zz:
            pw = [1]*(n+1)
            u = 1
            for q in range(n):
                pw[q+1] = u = u*bb % mm
            ___Hashinator.zz[key] = pw
        p._pw = ___Hashinator.zz[key]
    def spin(p, a, b):
        # Returns hash for [a,b)
        return (p._h[b] - p._h[a]*p._pw[b-a])%p.mm

def _solve(n, a, b):
    crazy_bitlen = max(max(a),max(b)).bit_length()
    ah, bh, cbh = [], [], []
    _BASE, _MOD = 641, int(1e9+7)
    for i in range(crazy_bitlen):
        ta, tb, tbn = [], [], []
        for aa, bb in zip(a,b):
            ta.append((aa>>i)&1)
            tb.append((bb>>i)&1)
            tbn.append(tb[-1]^1)
        ah.append(___Hashinator(ta,_BASE,_MOD))
        bh.append(___Hashinator(tb,_BASE,_MOD))
        cbh.append(___Hashinator(tbn,_BASE,_MOD))
    X = [0]*n
    for i in range(crazy_bitlen):
        for spot in range(n):
            lhs = ah[i].spin(spot, n)
            rhs = ah[i].spin(0, spot)
            if X[spot] is None:
                continue
            if lhs == cbh[i].spin(0, n-spot) and rhs == cbh[i].spin(n-spot, n):
                X[spot] += (1 << i)
            elif lhs == bh[i].spin(0, n-spot) and rhs == bh[i].spin(n-spot, n):
                pass
            else:
                X[spot] = None
    return ['{} {}'.format(ix,xv) for ix,xv in enumerate(X) if xv is not None]

main = lambda: print(*_solve(_i(), _il(), _il()), sep='\n')

if __name__=='__main__': main()