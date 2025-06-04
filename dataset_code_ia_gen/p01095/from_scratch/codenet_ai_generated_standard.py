import sys
import math

def prime_factors(n):
    factors = []
    for p in [2,3,5]:
        count = 0
        while n % p == 0:
            n //= p
            count += 1
        if count:
            factors.append((p,count))
    f = 7
    inc = [4,2,4,2,4,6,2,6]
    i = 0
    while f*f <= n:
        count = 0
        while n % f == 0:
            n //= f
            count += 1
        if count:
            factors.append((f,count))
        f += inc[i]
        i = (i+1)%8
    if n > 1:
        factors.append((n,1))
    return factors

def divisor_count(n):
    res = 1
    for _, c in prime_factors(n):
        res *= (c+1)
    return res

for line in sys.stdin:
    if line.strip()=='': continue
    m,n= map(int,line.split())
    if m==0 and n==0:
        break
    # find largest x >= m s.t divisor_count(x) <= n
    # upper bound for x can be m+n*log(m) for search
    # but here we do binary search between m and a large number
    left, right = m, 10**9
    ans = m
    while left <= right:
        mid = (left+right)//2
        if divisor_count(mid) <= n:
            ans = mid
            left = mid+1
        else:
            right = mid-1
    print(ans)