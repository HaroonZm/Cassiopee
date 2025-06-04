import sys
from functools import partial
from operator import mul

readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    from string import ascii_uppercase, ascii_lowercase

    s0 = '^' + ascii_uppercase + ascii_lowercase
    idx_map = s0.index

    S = list(map(idx_map, readline().strip()))
    T = list(map(idx_map, readline().strip()))
    N, M = len(S), len(T)

    base, mod = 59, 10**9 + 9

    # Precompute powers
    pw = [1]
    for _ in range(max(N, M)):
        pw.append(pw[-1] * base % mod)

    def prefix_hash(seq):
        # One-liner: cumulative hash
        return [0] + [h := (prev * base + x) % mod for prev, x in zip(prefix_hash(seq[:-1]), seq)] if seq else [0]
    # However, for efficiency and avoiding recursion limit:
    def prefix_hash_lin(seq):
        h = [0]
        for x in seq:
            h.append((h[-1] * base + x) % mod)
        return h

    hashT = prefix_hash_lin(T)
    hashS = prefix_hash_lin(S)

    ans = 0

    # Use inlined hash extraction lambda for concise advanced style
    get_hash = lambda h, l, r: (h[r] - h[l] * pw[r-l]) % mod

    range_nm = range(N - M + 1)

    # Using assignment expressions and early continue for optim
    for i in range_nm:
        l, r = 0, M + 1
        while (l1 := l + 1) < r:
            m = (l1 + r - 1) >> 1
            if get_hash(hashT, 0, m) == get_hash(hashS, i, i + m):
                l = m
            else:
                r = m
        if l < M and get_hash(hashT, l + 1, M) == get_hash(hashS, i + l + 1, i + M):
            ans += 1

    write(f"{ans}\n")

solve()