import os
import sys

import numpy as np

def solve(inp):
    def mod_pow(x, a, MOD):
        ret = 1
        cur = x
        while a:
            if a & 1:
                ret = ret * cur % MOD
            cur = cur * cur % MOD
            a >>= 1
        return ret

    h = inp[0]
    ppp = inp[1:]
    n = 1 << (h - 1)
    ppp += n - 1
    MOD = 10 ** 9 + 7

    cumprods = np.ones(2 * n, dtype=np.int64)
    cumprods_rev = np.ones(n, dtype=np.int64)
    cumprods_through = np.zeros(n, dtype=np.int64)
    for i in range(2, 2 * n):
        cumprods[i] = cumprods[i >> 1] * i % MOD
    for i in range(n):
        cumprods_rev[i] = mod_pow(cumprods[i], MOD - 2, MOD)
        cumprods_through[i] = cumprods[i + n] * cumprods[ppp[i]] % MOD

    cumprods_from_tree1 = np.zeros(2 * n, dtype=np.int64)
    ans = 0

    for lca in range(1, n):
        d = lca
        digit = h
        while d:
            d >>= 1
            digit -= 1

        leftmost_leaf_in_left_subtree = lca << digit
        leftmost_leaf_in_right_subtree = ((lca << 1) + 1) << (digit - 1)
        rightmost_leaf_in_right_subtree = (lca + 1) << digit

        rev = cumprods_rev[lca >> 1]
        for leaf in range(leftmost_leaf_in_left_subtree, leftmost_leaf_in_right_subtree):
            v = ppp[leaf - n]
            cp = cumprods_through[leaf - n] * rev % MOD
            while v > 1:
                cumprods_from_tree1[v] += cp * cumprods_rev[v >> 1] % MOD
                v >>= 1

        rev = cumprods_rev[lca]
        for leaf in range(leftmost_leaf_in_right_subtree, rightmost_leaf_in_right_subtree):
            v = ppp[leaf - n]
            cp = cumprods_through[leaf - n] * rev % MOD
            while v > 1:
                ans += cumprods_from_tree1[v ^ 1] % MOD * cp % MOD * cumprods_rev[v >> 2] % MOD
                v >>= 1
            ans %= MOD

        for leaf in range(leftmost_leaf_in_left_subtree, leftmost_leaf_in_right_subtree):
            v = ppp[leaf - n]
            while cumprods_from_tree1[v] != 0:
                cumprods_from_tree1[v] = 0
                v >>= 1

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
print(ans)