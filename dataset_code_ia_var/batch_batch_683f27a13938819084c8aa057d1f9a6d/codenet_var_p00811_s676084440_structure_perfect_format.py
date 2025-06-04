#!/usr/bin/env python

"""
Problems 1232
Problem A: Calling Extraterrestrial Intelligence Again
"""
import math

def eratosthenes(n):
    """
    エラトステネスのふるい
    """
    primes = [i for i in range(n + 1)]
    primes[1] = 0  # 1は素数ではない
    for prime in primes:
        if prime > math.sqrt(n):
            break
        if prime == 0:
            continue
        for non_prime in range(2 * prime, n + 1, prime):  # primeの分、合成数をふるいかけていく
            primes[non_prime] = 0  # 素数でない要素は0にする
    prime_list = []
    for prime in primes:
        if prime != 0:
            prime_list.append(prime)
    return prime_list

primes = eratosthenes(100000)

while True:
    m, a, b = map(int, input().split())
    if m <= 4 or a == 0 or b == 0:
        break
    p = 0
    q = 0
    max_s = 0
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            if primes[i] * primes[j] > m:
                break
            if a / b <= primes[i] / primes[j] <= 1:
                if primes[i] * primes[j] >= max_s:
                    max_s = primes[i] * primes[j]
                    p = primes[i]
                    q = primes[j]
    print("{0} {1}".format(p, q))