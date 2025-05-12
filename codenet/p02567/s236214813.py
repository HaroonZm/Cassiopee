import os
import sys

import numpy as np

def solve(inp):
    SEGTREE_TABLES = []

    def bit_length(n):
        ret = 0
        while n:
            n >>= 1
            ret += 1
        return ret

    def segtree_init(n):
        n2 = 1 << bit_length(n)
        SEGTREE_TABLES.append(np.zeros(n2 << 1, dtype=np.int64))
        return len(SEGTREE_TABLES) - 1

    def segtree_build(ins, arr):
        table = SEGTREE_TABLES[ins]
        offset = table.size >> 1
        table[offset:offset + len(arr)] = arr
        for i in range(offset - 1, 0, -1):
            ch = i << 1
            table[i] = max(table[ch], table[ch + 1])

    def segtree_update(ins, i, x):
        table = SEGTREE_TABLES[ins]
        offset = table.size >> 1
        i += offset
        table[i] = x
        while i > 1:
            ch = i
            i >>= 1
            table[i] = max(table[ch], table[ch ^ 1])

    def segtree_query(ins, l, r):
        """ max [l, r) """
        table = SEGTREE_TABLES[ins]
        offset = table.size >> 1
        l += offset
        r += offset
        res = -1
        while l < r:
            if r & 1:
                res = max(res, table[r - 1])
            if l & 1:
                res = max(res, table[l])
                l += 1
            l >>= 1
            r >>= 1
        return res

    def segtree_search(ins, lo, x):
        """
        Get min i where lo <= i, A[i] >= x.
        Assume that a sentinel larger than x is inserted at the right end.
        """
        table = SEGTREE_TABLES[ins]
        offset = table.size >> 1
        i = lo + offset
        while table[i] < x:
            while i & 1:
                i >>= 1
            i += 1
        while i < offset:
            i <<= 1
            if table[i] < x:
                i += 1
        return i - offset

    def segtree_debug_print(ins):
        table = SEGTREE_TABLES[ins]
        offset = table.size >> 1
        i = 1
        while i <= offset:
            print(table[i:2 * i])
            i <<= 1

    n = inp[0]
    q = inp[1]
    aaa = inp[2:n + 2]
    ttt = inp[n + 2::3]
    xxx = inp[n + 3::3]
    yyy = inp[n + 4::3]
    INF = 1 << 60

    aaa = np.append(aaa, INF)
    ins = segtree_init(n + 1)
    segtree_build(ins, aaa)

    ans = []

    for i in range(q):
        if ttt[i] == 1:
            segtree_update(ins, xxx[i] - 1, yyy[i])
        elif ttt[i] == 2:
            res = segtree_query(ins, xxx[i] - 1, yyy[i])
            ans.append(res)
        else:
            res = segtree_search(ins, xxx[i] - 1, yyy[i])
            ans.append(res + 1)

    return ans

if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC

    cc = CC('my_module')
    cc.export('solve', '(i8[:],)')(solve)
    cc.compile()
    exit()

if os.name == 'posix':
    # noinspection PyUnresolvedReferences
    from my_module import solve
else:
    from numba import njit

    solve = njit('(i8[:],)', cache=True)(solve)
    print('compiled', file=sys.stderr)

inp = np.fromstring(sys.stdin.read(), dtype=np.int64, sep=' ')
ans = solve(inp)
print('\n'.join(map(str, ans)))