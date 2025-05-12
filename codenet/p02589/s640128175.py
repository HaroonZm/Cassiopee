import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def main(S):
    S = S.copy()
    l_ind = np.where(S == -1)[0][:-1] + 1
    r_ind = np.where(S == -1)[0][1:]

    # 逆順にしておく
    N = len(l_ind)
    for i in range(N):
        S[l_ind[i]:r_ind[i]] = S[l_ind[i]:r_ind[i]][::-1]

    # Trie木の構築
    path = np.zeros_like(S)
    child = np.zeros((len(S), 26), np.int64)
    is_end = np.zeros(len(S), np.bool_)

    n_node = 1
    for i in range(N):
        node = 0
        for j in range(l_ind[i], r_ind[i]):
            path[j] = node
            if child[node][S[j]] == 0:
                child[node][S[j]] = n_node
                n_node += 1
            node = child[node][S[j]]
        is_end[node] = True
    child = child[:n_node]
    is_end = is_end[:n_node]
    ans = 0
    for i in range(N):
        se = 0
        for j in range(r_ind[i] - 1, l_ind[i] - 1, -1):
            se |= 1 << S[j]
            node = path[j]
            for k in range(26):
                if se & 1 << k:
                    if is_end[child[node][k]]:
                        ans += 1
    return ans - N

if sys.argv[-1] == 'ONLINE_JUDGE':
    import numba
    from numba import njit, b1, i4, i8, f8
    import numba
    from numba.pycc import CC
    cc = CC('my_module')

    def cc_export(f, signature):
        cc.export(f.__name__, signature)(f)
        return numba.njit(f)

    main = cc_export(main, (i8[:],))
    cc.compile()

from my_module import main

N = int(readline())
S = np.array(list(read().rstrip()), np.int64)

S[S == ord('\n')] = -1
S[S > 0] -= ord('a')
S = np.insert(S, 0, -1)
S = np.append(S, -1)

print(main(S))