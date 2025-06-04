import sys
import numpy as np
from functools import reduce
from itertools import accumulate, count, islice, dropwhile
from operator import itemgetter, mul

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def choose_increasing(q):
    def reducer(acc, x):
        idx = next(islice(dropwhile(lambda i: acc[i] < x, range(len(acc) - 1, -1, -1)), 1), None)
        if idx is not None:
            del acc[idx + 1:]
        acc.append(x)
        return acc
    return np.array(reduce(lambda acc, x: reducer(acc, x) or acc, q, []), np.int64)

def main(A, N):
    # Using a dict as a pseudo-heap with in-place min extraction
    heap = {len(A): [(-A[-1], 1)]}
    for idx, n in enumerate(A[::-1]):
        h = heap.setdefault(idx, [])
        src = heap[idx - 1] if idx > 0 else [(-A[-1], 1)]
        while src:
            x, coef = src.pop()
            if -x <= n:
                h.append((x, coef))
                continue
            total_coef = coef + sum(c for x2, c in list(src) if x2 == x)
            src[:] = [(x2, c2) for x2, c2 in src if x2 != x]
            q, r = divmod(-x, n)
            h.append((-n, total_coef * q))
            h.append((-r, total_coef))
    # Unroll all heap lists
    ret = np.zeros(N + 10, dtype=np.int64)
    for heaplist in heap.values():
        for x, c in heaplist:
            x = -x
            ret[1] += c
            ret[x + 1] -= c
    return np.fromiter(accumulate(ret), dtype=np.int64)[1:N+1]

if sys.argv[-1] == 'ONLINE_JUDGE':
    import numba as nb
    from numba.pycc import CC
    cc = CC('my_module')
    def cc_export(f, signature):
        cc.export(f.__name__, signature)(f)
        return nb.njit(f)
    main = cc_export(main, (nb.int64[:], nb.int64))
    cc.compile()

from my_module import main

N, Q = map(int, readline().split())
q = [N] + list(map(int, read().split()))
A = choose_increasing(q)
ans = main(A, N)
print('\n'.join(map(str, map(int, ans))))