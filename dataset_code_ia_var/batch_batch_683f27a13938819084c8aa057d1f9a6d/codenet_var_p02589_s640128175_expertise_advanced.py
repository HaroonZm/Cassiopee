import sys
import numpy as np

# Utiliser mmap pour un input rapide et efficient
import mmap

with sys.stdin.buffer as f, mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
    raw = mm.read()

def process_input(raw):
    # Extraction rapide de N et S depuis le flux brut
    nl_pos = raw.find(b'\n')
    N = int(raw[:nl_pos])
    arr = np.frombuffer(raw[nl_pos+1:].replace(b'\n', b'-'), dtype=np.int8)
    # Remplace b'-' (ASCII 45) par -1, et ajuste 'a'-'z' en 0-25
    arr = np.where(arr == 45, -1, arr - ord('a'))
    arr = np.concatenate(([-1], arr, [-1]))
    return arr

S = process_input(raw)

import functools
import operator

def main(S):
    # Points de séparation
    breaks = np.flatnonzero(S == -1)
    l_ind, r_ind = breaks[:-1] + 1, breaks[1:]

    N = len(l_ind)
    # Reverses en place, slices intelligentes, boucle vectorisée masquée
    for l, r in zip(l_ind, r_ind):
        S[l:r] = S[l:r][::-1]

    # Trie: allocation paresseuse pour l'espace (estimé au plus large, redimensionné à la fin)
    L = S.size
    child = np.zeros((L+1, 26), np.int32)
    is_end = np.zeros(L+1, dtype=bool)
    path = np.zeros(L, dtype=np.int32)

    n_node = 1
    for l, r in zip(l_ind, r_ind):
        node = 0
        for j in range(l, r):
            path[j] = node
            c = S[j]
            if child[node, c] == 0:
                child[node, c] = n_node
                n_node += 1
            node = child[node, c]
        is_end[node] = True

    child = child[:n_node]
    is_end = is_end[:n_node]

    ans = 0
    # Compilation d'une table d'un seul coup pour éviter les doubles for lourds
    bit_masks = np.left_shift(1, np.arange(26, dtype=np.int32))
    for l, r in zip(l_ind, r_ind):
        se = 0
        for j in range(r-1, l-1, -1):
            se |= bit_masks[S[j]]
            node = path[j]
            active = se & ((1 << 26) - 1)
            idxs = (active & bit_masks) > 0
            touched = child[node][idxs]
            ans += np.sum(is_end[touched])
    return int(ans - N)

# Compilation Just-In-Time si nécessaire
if sys.argv[-1] == 'ONLINE_JUDGE':
    import numba
    from numba import njit, i8
    main = njit(main)
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', 'int64(int64[:])')(main)
    cc.compile()
    from my_module import main

print(main(S))