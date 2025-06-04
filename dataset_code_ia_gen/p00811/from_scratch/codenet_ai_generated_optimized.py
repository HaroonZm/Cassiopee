import sys
import math

MAX_M = 100000

# Sieve of Eratosthenes to generate primes up to MAX_M
sieve = [True]*(MAX_M+1)
sieve[0] = sieve[1] = False
for i in range(2,int(MAX_M**0.5)+1):
    if sieve[i]:
        for j in range(i*i, MAX_M+1, i):
            sieve[j] = False
primes = [i for i,v in enumerate(sieve) if v]

# For fast prime checks
prime_set = set(primes)

input_lines = sys.stdin.read().splitlines()
for line in input_lines:
    m,a,b = map(int,line.strip().split())
    if m==0 and a==0 and b==0:
        break
    best_area = 0
    best_p = best_q = 0
    # Because p/q <= 1 => p <= q, and p/q >= a/b => p * b >= q * a
    # We'll try q from largest prime <= m down to 2
    # For each q, we try to find largest p prime satisfying:
    # p*b >= q*a AND p <= q AND p*q <= m
    # We'll iterate q downward and for each q binary search or iterate p downward.
    # Since a/b <= 1, p ≤ q
    # Start from max prime q ≤ m
    idx_q = 0
    # find max pos where prime <= m
    # binary search for q
    left, right = 0, len(primes)-1
    while left<=right:
        mid = (left+right)//2
        if primes[mid] <= m:
            idx_q = mid
            left = mid + 1
        else:
            right = mid -1
    for i in range(idx_q, -1, -1):
        q = primes[i]
        if q*q <= best_area:
            # since p ≤ q and p*q <= m and area ≤ best_area, no need to continue for smaller q
            break
        # minimal p from ratio:
        # p/b >= q*a/b => p >= ceil(q*a/b)
        mn_p = (q*a + b -1)//b
        if mn_p > q:
            # p ≤ q so no valid p
            continue
        # p*q ≤ m => p ≤ m//q
        max_p = min(q, m//q)
        if max_p < mn_p:
            continue
        # search largest prime p between mn_p and max_p
        # binary search in primes for max_p
        left_p = 0
        right_p = len(primes)-1
        idx_max_p = -1
        while left_p<=right_p:
            mid = (left_p+right_p)//2
            if primes[mid] <= max_p:
                idx_max_p = mid
                left_p = mid+1
            else:
                right_p = mid-1
        # now move idx_max_p down until primes[idx_max_p] >= mn_p
        while idx_max_p >=0 and primes[idx_max_p] >= mn_p:
            p = primes[idx_max_p]
            if p*b >= q*a:
                area = p*q
                if area > best_area or (area == best_area and (p<best_p or (p==best_p and q<best_q))):
                    best_area = area
                    best_p = p
                    best_q = q
                break
            idx_max_p -=1
    print(best_p,best_q)