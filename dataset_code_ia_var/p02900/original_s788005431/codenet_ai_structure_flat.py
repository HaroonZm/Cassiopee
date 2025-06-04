import sys
import math

A, B = map(int, sys.stdin.readline().split())
gcd = math.gcd(A, B)
if gcd == 1:
    print(1)
else:
    n = gcd
    cnt = 0
    m = 2
    while m * m <= n:
        if n % m == 0:
            cnt += 1
            while n % m == 0:
                n //= m
        m = m + 1 if m == 2 else m + 2
    if n > 1:
        cnt += 1
    print(cnt + 1)