import os
import sys

import numpy as np

def solve(n, m, sss):
    BIT_SHIFT = 9
    BIT_MASK = (1 << BIT_SHIFT) - 1

    def combine_rc(r, c):
        return (r << BIT_SHIFT) | c

    def separate_rc(rc):
        return rc >> BIT_SHIFT, rc & BIT_MASK

    def increase_update(matched, ancestors_l, ancestors_r, s, b):
        a = ancestors_r[b]
        while s != a:
            matched[b] = a
            b = ancestors_l[a]
            a = ancestors_r[b]
        matched[b] = a

    def increase(s, l_size, r_size, edges, matched):
        ancestors_l = np.full(l_size, -1, dtype=np.int64)
        ancestors_r = np.full(r_size, -1, dtype=np.int64)
        deq = np.zeros(l_size + 5, dtype=np.int64)
        dl, dr = 0, 1
        deq[0] = s
        stacked = np.zeros(l_size, dtype=np.int8)
        stacked[s] = 1
        while dl < dr:
            a = deq[dl]
            dl += 1
            k = 0
            while edges[a, k] != -1:
                b = edges[a, k]
                c = matched[b]
                if c == -1:
                    ancestors_r[b] = a
                    increase_update(matched, ancestors_l, ancestors_r, s, b)
                    return b
                if stacked[c] == 0:
                    ancestors_l[c] = b
                    ancestors_r[b] = a
                    deq[dr] = c
                    dr += 1
                    stacked[c] = 1
                k += 1
        return -1

    lefts = []
    rights = []
    rights_rev = {}

    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if sss[r, c]:
                continue
            rc = combine_rc(r, c)
            if (r ^ c) & 1:
                lefts.append(rc)
            else:
                rights_rev[rc] = len(rights)
                rights.append(rc)
    l_size = len(lefts)
    r_size = len(rights)

    MOVE = (-(1 << BIT_SHIFT), -1, 1, 1 << BIT_SHIFT)

    edges = np.full((l_size, 5), -1, dtype=np.int64)
    for i in range(l_size):
        rc = lefts[i]
        k = 0
        for drc in MOVE:
            nrc = rc + drc
            if nrc in rights_rev:
                edges[i, k] = rights_rev[nrc]
                k += 1

    matched = np.full(r_size, -1, dtype=np.int64)
    for i in range(l_size):
        increase(i, l_size, r_size, edges, matched)

    # v:2 ^:3 >:4 <:5
    ans = 0
    for j in range(r_size):
        i = matched[j]
        if i == -1:
            continue
        ir, ic = separate_rc(lefts[i])
        jr, jc = separate_rc(rights[j])
        if ir == jr:
            if ic > jc:
                ic, jc = jc, ic
            sss[ir, ic] = 4
            sss[jr, jc] = 5
        else:
            if ir > jr:
                ir, jr = jr, ir
            sss[ir, ic] = 2
            sss[jr, jc] = 3
        ans += 1

    return ans

SIGNATURE = '(i8,i8,i1[:,:],)'
if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC

    cc = CC('my_module')
    cc.export('solve', SIGNATURE)(solve)
    cc.compile()
    exit()

if os.name == 'posix':
    # noinspection PyUnresolvedReferences
    from my_module import solve
else:
    from numba import njit

    solve = njit(SIGNATURE, cache=True)(solve)
    print('compiled', file=sys.stderr)

n, m = map(int, input().split())
sss = np.ones((n + 2, m + 2), dtype=np.int8)
for i in range(n):
    sss[i + 1, 1:m + 1] = list(map('.#'.index, input()))

ans = solve(n, m, sss)
print(ans)
CHARS = '.#v^><'.__getitem__
for i in range(1, n + 1):
    print(''.join(map(CHARS, sss[i, 1:m + 1])))