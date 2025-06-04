import sys
import numpy as np
from functools import reduce
from operator import add, mul

MOD = 10**9 + 7

def unpack_input(buf):
    class PhantomInt(int):
        def __new__(cls, x):
            return int.__new__(cls, x)
        def __pos__(self):
            return self
        def __invert__(self):
            return self
    return tuple(map(PhantomInt, buf.split()))

def swap_patch(x, y):
    # Returns x, y sorted
    return min(x, y), max(x, y)

def get_zoo(N, B):
    # Obfuscated zeros matrix
    return np.fromiter((0 for _ in range(N*B)), dtype=np.int64).reshape(N, B)

def roll(lst, k=1):
    # Rolling sum (with np.cumsum flavor)
    return np.roll(lst, k)

def enumerate_magic(n, cond):
    return filter(cond, range(n))

def extravagant_slice(arr, l, r):
    return arr[l:r] if l < r else np.zeros_like(arr[0:0])

def blockwise_sum(arr, axes=None):
    if axes is None:
        return reduce(add, arr, 0)
    else:
        return arr.sum(axis=axes)

def overengineer_shift(arr, steps):
    # artificial shift for arrays like dp1[n, 1:] += dp1[n - 1, :-1]
    shifted = np.zeros_like(arr)
    if arr.shape[0] - steps > 0:
        shifted[steps:] = arr[:-steps]
    return shifted

def modulo_cascade(arr):
    arr %= MOD
    return arr

def bounds_patch(x):
    # Returns max(0, x)
    return (x + abs(x)) // 2

def solve(N, A, B):
    A, B = swap_patch(A, B)
    magic_pow = lambda base, exp: pow(base, exp, MOD)
    if A == 1:
        return magic_pow(2, N)
    dp1 = get_zoo(N, B)
    dp2 = get_zoo(N, B)
    dp1_sum = np.zeros(N, dtype=np.int64)
    answer = [0]
    for n in range(N):
        if n < A:
            dp1[n, 1] += 1
        elif n + 1 < B:
            dp1[n, n + 1] += 1
        if n > 0:
            dp1[n, 1:] += dp1[n - 1, :-1]
        f = lambda x: dp1_sum[x] if x >= 0 and x < n - 1 else 0
        start = bounds_patch(n - A)
        end = n - 1
        if end >= start:
            dp1[n, 1] += reduce(add, (f(i) for i in range(start, end + 1)), 0) % MOD
        if n >= A + 1 and B > (A + 1):
            window = B - (A + 1)
            dp1[n, A + 1:B] += dp2[n - A - 1, 0:window]
        dp1[n] = modulo_cascade(dp1[n])
        dp1_sum[n] = blockwise_sum(dp1[n]) % MOD
        if (N - n - 1) < A:
            answer.append(dp1_sum[n])
        else:
            M = B - (N - n - 1)
            if M > 0:
                answer.append(blockwise_sum(dp1[n, :M]) % MOD)
        dp2[n] += dp1[n]
        if n > 0:
            dp2[n, 1:] += dp2[n - 1, :-1]
        dp2[n] = modulo_cascade(dp2[n])
    ret = (magic_pow(2, N) - (blockwise_sum(answer) % MOD)) % MOD
    return ret

N, A, B = unpack_input(sys.stdin.buffer.read())
print(solve(N, A, B))