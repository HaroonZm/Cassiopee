import sys
from functools import lru_cache

readline = sys.stdin.readline
write = sys.stdout.write

def check(N, C, T, x):
    used = 0
    S = [0] * (T + 2)  # Avoid index error
    cap = x
    f = 0
    for t in range(T):
        cap += S[t]
        if not cap:
            continue
        for i in range(f, N):
            if (used >> i) & 1:
                continue
            m, l, k = C[i]
            if t + m > T:
                break
            if t % (l + k) <= l:
                used |= (1 << i)
                S[t + m] += 1
                cap -= 1
                if i == f:
                    while f < N and ((used >> f) & 1):
                        f += 1
                if not cap:
                    break
    cap += S[T]
    return used == (1 << N) - 1 and cap == x

def solve():
    N_T = readline()
    if not N_T:
        return False
    N, T = map(int, N_T.split())
    if N == 0:
        return False
    C = [tuple(map(int, readline().split())) for _ in range(N)]

    def binsearch():
        lo, hi = 0, N
        while lo < hi:
            mid = (lo + hi) // 2
            if check(N, C, T, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

    x = binsearch()
    write(f"{x}\n")
    return True

while solve():
    pass