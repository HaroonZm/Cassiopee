import sys
import numpy as np

N = int(sys.stdin.buffer.readline())
AK = np.array(sys.stdin.buffer.read().split(), np.int32)
A = AK[::2]
K = AK[1::2]
G = 0

t = 0
while t < 50000:
    q = A // K
    r = A % K
    q = q + 1
    r = r + (-r) % q
    A = A - r
    if t % 1000 == 0:
        ind = r != 0
        if np.count_nonzero(~ind):
            G = G ^ np.bitwise_xor.reduce(A[~ind] // K[~ind])
            A = A[ind]
            K = K[ind]
            if len(A) == 0:
                break
    t = t + 1

if G:
    print('Takahashi')
else:
    print('Aoki')