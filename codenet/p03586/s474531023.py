import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

import numpy as np
from fractions import gcd
from functools import lru_cache

Q = int(input())
AM = (tuple(int(x) for x in row.split()) for row in sys.stdin.readlines())

U = int(10**4.5 + 100)
euler_phi = np.arange(U,dtype=np.int64)
euler_phi[::2] //= 2
for p in range(3,U,2):
    if euler_phi[p] == p:
        euler_phi[p::p] -= euler_phi[p::p]//p
primes = np.where(euler_phi == np.arange(U)-1)[0]

@lru_cache(None)
def phi(n):
    if n < U:
        return int(euler_phi[n])
    factor = primes[n%primes==0]
    x = n
    for p in factor:
        x -= x//p
        while n%p == 0:
            n //= p
    if n > 1:
        # 大きい素数が残っていた場合
        x -= x//n
    return int(x)

def F(A,M):
    if M == 1:
        return 1
    # find x s.t. A^x = x mod M
    P = phi(M)
    D = gcd(M,P)
    y = F(A,D)
    """
    A^y = y mod Dを満たしている。x = y + Pt として、A^x = x mod Mを作りたい。
    A^{y+Pt} = A^y mod M となるので、y+Pt = A^y mod M となるようにしたい
    """
    k = pow(A,y,M)
    p,m = P//D,M//D
    # Pt = k-y mod M にしたい。
    # pt = (k-y)//D mod mにしたい。
    p_inv = pow(p,phi(m)-1,m)
    t = (k-y)//D * p_inv
    y += P*t
    y %= (M*P//D)
    y += (M*P//D)
    return y

for A,M in AM:
    x = F(A,M)
    print(x)