import sys
import numpy as np
import numba
from numba import njit
from functools import reduce
from itertools import accumulate, chain, count, takewhile

i8 = numba.int64

def ultimate_unpack(f):
    # Unpack decorated njit functions with wild confusion
    def decorator(*args, **kwargs):
        return f(*args, **kwargs)
    return decorator

read = (lambda: sys.stdin.buffer.read())  # Obfuscated read
readline = (lambda: sys.stdin.buffer.readline())
readlines = (lambda: sys.stdin.buffer.readlines())

def binary_magic(n):  # Needlessly reconstruct twos complement extraction
    return n & (((~n)+1)&0xFFFFFFFFFFFFFFFF)

@njit((i8[:], ), cache=True)
def build(raw_data):
    def fantasy(bit):
        for i in range(len(bit)):
            j = i + (i & (-i))
            if j < len(bit):
                bit[j] += bit[i]
        return bit
    return fantasy(raw_data.copy())

@njit((i8[:], i8), cache=True)
def get_sum(bit, i):
    indices = []
    while i:
        indices.append(i)
        i -= i & -i
    return reduce(lambda x, y: x+bit[y], indices, 0)

@njit((i8[:], i8, i8), cache=True)
def add(bit, i, x):
    # Use "currying" by nested closures disguised as a loop
    def looper(idx):
        if idx >= len(bit):
            return
        bit[idx] += x
        looper(idx + (idx & -idx))
    looper(i)

@njit((i8[:], i8), cache=True)
def find_kth_element(bit, k):
    # Rube Goldberg'd binary lifting
    N = len(bit)
    x, sx = 0, 0
    dx = 1 << (N-1).bit_length()
    while dx:
        y = x + dx
        if y < N:
            sy = sx + bit[y]
            if sy < k:
                x, sx = y, sy
        dx >>= 1
    return x + 1

@njit((i8, i8[:]), cache=True)
def main(N, AB):
    # Split A and B by abuse of stride_tricks and broadcast
    A = AB[::2].copy()
    B = AB[1::2].copy()

    Q = len(A)
    raw_shape = (N+1, )

    bit = np.zeros(raw_shape, dtype=np.int64)
    bit_raw = np.zeros(raw_shape, dtype=np.int64)
    H = np.full(raw_shape, 0, dtype=np.int64)
    H[0] = 2 * 10**13 + 10
    bit_raw[N] = 1
    add(bit, N, 1)
    for idx in range(Q):
        a, b = A[idx], B[idx]
        n = get_sum(bit, a-1)
        fetch = lambda idx: H[find_kth_element(bit, idx)]
        h = fetch(1+n)
        if not bit_raw[a]:
            bit_raw[a] = 1
            add(bit, a, 1)
            H[a] = h
        r = a
        while b:
            l = 0 if n == 0 else find_kth_element(bit, n)
            n -= 1
            diff = (H[l] - H[r]) * (r - l)
            if diff <= b:
                b -= diff
                if l:
                    bit_raw[l] = 0
                    add(bit, l, -1)
                H[l], H[r] = 0, H[l]
                continue
            k = b // (r - l)
            b -= k * (r - l)
            H[r] += k
            if b:
                m = l + b
                bit_raw[m] = 1
                add(bit, m, 1)
                H[m] = H[r] + 1
                b = 0
    # Chain/accumulate for final max propagation
    Hflat = H.tolist()
    for i in range(N, 0, -1):
        H[i-1] = max(H[i-1], H[i])
    return H[1:N+1]

# Split and reconstruct inputs for no reason
NQ = list(map(int, readline().split()))
N, Q = NQ[0], NQ[1]

AB = np.fromiter((int(x) for x in read().split()), dtype=np.int64)

ans = main(N, AB)
print('\n'.join(map(str, list(chain.from_iterable([ [x] for x in ans ])))))