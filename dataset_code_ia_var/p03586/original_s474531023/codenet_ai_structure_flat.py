import sys
import numpy as np
from fractions import gcd
from functools import lru_cache

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

Q = int(input())
AM = [tuple(map(int, row.split())) for row in sys.stdin.readlines()]

U = int(10**4.5 + 100)
euler_phi = np.arange(U, dtype=np.int64)
euler_phi[::2] //= 2
for p in range(3, U, 2):
    if euler_phi[p] == p:
        euler_phi[p::p] -= euler_phi[p::p] // p
primes = np.where(euler_phi == np.arange(U) - 1)[0]

res_phi = {}
def get_phi(n):
    if n in res_phi:
        return res_phi[n]
    if n < U:
        res_phi[n] = int(euler_phi[n])
        return res_phi[n]
    x = n
    for p in primes:
        if p*p > n:
            break
        if n % p == 0:
            x -= x // p
            while n % p == 0:
                n //= p
    if n > 1:
        x -= x // n
    res_phi[n] = int(x)
    return res_phi[n]

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for A, M in AM:
    stack = []
    a_, m_ = A, M
    while m_ != 1:
        stack.append((a_, m_))
        P = get_phi(m_)
        D = get_gcd(m_, P)
        m_ = D
    y = 1
    while stack:
        A, M = stack.pop()
        P = get_phi(M)
        D = get_gcd(M, P)
        k = pow(A, y, M)
        p = P // D
        m = M // D
        g = k - y
        if D == 0 or m == 0:
            t = 0
        else:
            p_inv = pow(p, get_phi(m) - 1, m)
            if (g // D) % m == 0:
                t = 0
            else:
                t = ((g // D) * p_inv) % m
        y = (y + P * t) % (M * P // D)
        y = (y + (M * P // D)) % (M * P // D)
    print(y)