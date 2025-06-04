import numpy as np
from scipy.signal import fftconvolve

def main():
    import sys
    n = sys.stdin.readline()
    lst = [int(x) for x in sys.stdin.readline().split()]
    A = np.asarray(lst, dtype=np.int64)

    MODULUS = 200003
    BASE = 2

    c = np.zeros(MODULUS, np.int64); d = np.zeros(MODULUS, np.int64)

    factor = 1
    for idx in range(MODULUS - 1):
        c[factor] = idx
        d[idx] = factor
        factor = (factor * BASE) % MODULUS

    B = [0.0] * MODULUS
    for v in A:
        if v > 0:
            idx = int(c[v])
            B[idx] += 1.0

    result = fftconvolve(B, B)
    total = 0
    i = 0
    while i < len(result):
        r = result[i]
        if r > 0.5:
            val = int(round(r))
            total += val * d[i % (MODULUS - 1)]
        i += 1

    for v in A.tolist() if hasattr(A, 'tolist') else A:
        total -= (v * v) % MODULUS

    ans = total // 2

    print(ans)

if __name__ == '__main__': main()