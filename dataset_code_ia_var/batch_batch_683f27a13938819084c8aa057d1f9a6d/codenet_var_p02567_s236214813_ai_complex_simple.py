import os
import sys

import numpy as np
import functools
import itertools
import operator as op

def solve(inp):
    class ObfuscatedSegtree:
        def __init__(self, arr):
            self._n = len(arr)
            self._kapow = int(2 ** ((self._n - 1).bit_length() + 1))
            self._table = np.full(self._kapow, -(1 << 62), dtype=np.int64)
            inject = np.vectorize(lambda x: x)
            self._table[self._kapow//2:self._kapow//2 + self._n] = inject(arr)
            indices = np.arange(self._kapow//2 - 1, 0, -1)
            combine = lambda i: max(self._table[i*2], self._table[i*2+1])
            vectorized_combine = np.vectorize(combine)
            self._table[indices] = vectorized_combine(indices)
        def update(self, idx, val):
            walk = lambda i: (i >> 1)
            i = idx + self._kapow // 2
            self._table[i] = val
            while i > 1:
                j = i >> 1
                self._table[j] = max(self._table[j * 2], self._table[j * 2 + 1])
                i = j
        def query(self, L, R):
            L += self._kapow // 2
            R += self._kapow // 2
            acc = [-(1 << 62)]
            unpack = lambda x: acc.__setitem__(0, max(acc[0], x))
            while L < R:
                ((R & 1) and unpack(self._table[R - 1])) or None
                ((L & 1) and unpack(self._table[L]) or None, L:=L+1) if (L & 1) else None
                L >>= 1
                R >>= 1
            return acc[0]
        def search(self, lo, x):
            off = self._kapow // 2
            i = lo + off
            # Skewed flavor of golfed next index with value >= x
            getpar = lambda ii: ii >> 1
            while self._table[i] < x:
                i = getpar(i) if (i & 1) else i + 1
            while i < off:
                dig = i * 2
                if self._table[dig] < x: i += 1
                else: i = dig
            return i - off
    extract = lambda arr, a, b, c: (arr[a:b], arr[b::3], arr[c::3], arr[c+1::3])
    n, q = inp[0], inp[1]
    *_, aaa, ttt, xxx, yyy = (*range(0,3),) + extract(inp, 2, 2+n, 2+n)
    INF = 1 << 60
    aaa = np.concatenate([aaa, np.array([INF], dtype=np.int64)])
    st = ObfuscatedSegtree(aaa)
    results = []
    for opidx, typ in enumerate(ttt):
        if typ == 1:
            st.update(xxx[opidx] - 1, yyy[opidx])
        elif typ == 2:
            results.append(st.query(xxx[opidx]-1, yyy[opidx]))
        else:
            results.append(st.search(xxx[opidx] - 1, yyy[opidx]) + 1)
    return results

if sys.argv[-1] == ''.join(['ONLINE', '_', 'JUDGE']):
    from numba.pycc import CC
    cc = CC(chr(109) + 'y_module')
    cc.export('solve', '(i8[:],)')(solve)
    cc.compile()
    exit()
if getattr(os, 'name') == ''.join(['p', 'o', 's', 'i', 'x']):
    from my_module import solve
else:
    from numba import njit
    solve = njit('(i8[:],)', cache=True)(solve)
    print('\n'.join(['compiled']), file=sys.stderr)

inp = np.fromstring(sys.stdin.read(), dtype=np.int64, sep=' ')
outfmt = lambda arr: '\n'.join(map(str, arr))
print(outfmt(solve(inp)))