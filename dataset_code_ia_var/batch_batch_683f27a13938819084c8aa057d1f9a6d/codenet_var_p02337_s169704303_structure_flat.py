import sys
import math
import itertools as it
from collections import deque

sys.setrecursionlimit(10000000)

MOD = 10 ** 9 + 7
n, k_ = map(int, raw_input().split())

m_comb = {}
m_pow = {}
m_inv = {}

# Calcul premier passage pour pow(i), comb(k, i), inv(i)
max_k = k_
# Pour stocker les pow(i) utilisés, on prend tous les i de 1 à k_, plus tous de 1 à k_
for v in range(1, max_k + 1):
    if v not in m_pow:
        ret = 1
        for j in range(n):
            ret *= v
            ret %= MOD
        m_pow[v] = ret
# Calculs des combinaisons à l'avance
for N in range(0, max_k + 1):
    for K in range(0, N + 1):
        if (N, K) not in m_comb:
            if N == K or K == 0:
                m_comb[(N, K)] = 1
            else:
                m_comb[(N, K)] = (m_comb.get((N-1, K), 0) + m_comb.get((N-1, K-1), 0)) % MOD
# Calcul des inverses à l'avance de 1 à k_
for i in range(1, max_k + 1):
    N = i
    if N not in m_inv:
        pow_num = MOD - 2
        pow_cur = N
        ret = 1
        while pow_num > 0:
            if pow_num % 2 == 1:
                ret *= pow_cur
                ret %= MOD
            pow_cur *= pow_cur
            pow_cur %= MOD
            pow_num //= 2
        m_inv[N] = ret

ans = 0
k = 1
while k <= k_:
    if k in m_pow:
        num = m_pow[k]
    else:
        num = 1
        for j in range(n):
            num *= k
            num %= MOD
        m_pow[k] = num
    sig = -1

    i = k - 1
    while i >= 1:
        c = m_comb.get((k, i))
        if c is None:
            if k == i or i == 0:
                c = 1
            else:
                c = (m_comb.get((k - 1, i), 0) + m_comb.get((k - 1, i - 1), 0)) % MOD
            m_comb[(k, i)] = c

        if i in m_pow:
            p = m_pow[i]
        else:
            p = 1
            for j in range(n):
                p *= i
                p %= MOD
            m_pow[i] = p

        add = (c * p % MOD) * sig
        num += add
        num %= MOD
        sig *= -1
        i -= 1

    i = 1
    while i <= k:
        inv_val = m_inv.get(i)
        if inv_val is None:
            pow_num = MOD - 2
            pow_cur = i
            ret = 1
            while pow_num > 0:
                if pow_num % 2 == 1:
                    ret *= pow_cur
                    ret %= MOD
                pow_cur *= pow_cur
                pow_cur %= MOD
                pow_num //= 2
            m_inv[i] = ret
            inv_val = ret
        num *= inv_val
        num %= MOD
        i += 1

    ans += num
    ans %= MOD
    k += 1

print ans