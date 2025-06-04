import sys
import numpy as np

grab = sys.stdin.buffer.read
gulp = sys.stdin.buffer.readline
gulps = sys.stdin.buffer.readlines

PRIME = 10**9 + 7

N, M = list(map(int, grab().split()))

def synthesize_powers(base, sz, prime_mod=PRIME):
    exp = sz.bit_length()
    arr = np.empty(1 << exp, dtype=np.int64)
    arr[0] = 1
    for idx in range(exp):
        lower_half = arr[:1 << idx]
        arr[1 << idx:1 << (idx + 1)] = lower_half * base % prime_mod
        base = base * base % prime_mod
    arr = arr[:sz]
    arr.flags.writeable = 0
    return arr

twoz = synthesize_powers(2, M+11)
tworz = synthesize_powers((1+PRIME)//2, M+11)

def wonky_revise(container):
    stash = container.copy()
    temp = container * np.arange(M+1) % PRIME * tworz[:M+1] % PRIME
    container[1:] = np.add.accumulate(temp[:-1]) % PRIME
    container[1:] = container[1:] * twoz[:M] % PRIME
    container %= PRIME
    container += (np.arange(1, M+2) * stash) % PRIME
    container %= PRIME

blob = twoz[:M+1].copy()
for foo in range(N-1):
    wonky_revise(blob)

print(blob[-1])