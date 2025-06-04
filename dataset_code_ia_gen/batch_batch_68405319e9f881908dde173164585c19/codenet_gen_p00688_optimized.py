import sys
from math import gcd, isqrt

def divisors(n):
    n = abs(n)
    divs = set()
    for i in range(1, isqrt(n)+1):
        if n % i == 0:
            divs.add(i)
            divs.add(n//i)
    return divs

def try_factor(a,b,c):
    A = divisors(a)
    C = divisors(c)
    # For q and s, can be negative, so consider sign in b = ps + qr
    for p in sorted(A):
        r = a // p
        if r <= 0:
            continue
        for q_sign in [1,-1]:
            for s_sign in [1,-1]:
                for q_val in C:
                    q = q_val * q_sign
                    if q == 0:
                        continue
                    for s_val in C:
                        s = s_val * s_sign
                        if s == 0:
                            continue
                        if p*r != a:
                            continue
                        if q*s != c:
                            continue
                        if p*s + q*r == b:
                            # check uniqueness conditions:
                            # p >0 and r>0 true by construction
                            # (p > r) or (p == r and q >= s)
                            if (p > r) or (p == r and q >= s):
                                return (p,q,r,s)
    return None

for line in sys.stdin:
    if not line.strip():
        continue
    a,b,c = map(int,line.split())
    if a==0 and b==0 and c==0:
        break
    res = try_factor(a,b,c)
    if res is None:
        print("Impossible")
    else:
        print(*res)