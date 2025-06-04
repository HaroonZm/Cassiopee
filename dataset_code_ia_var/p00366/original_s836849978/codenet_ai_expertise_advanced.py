from sys import stdin
from bisect import bisect_left
from math import isqrt

n = int(stdin.readline())
lis = [int(stdin.readline()) for _ in range(n)]
cou = max(lis)

# Optimized divisor extraction using set and sqrt
divisors = set()
for i in range(1, isqrt(cou) + 1):
    if cou % i == 0:
        divisors.add(i)
        divisors.add(cou // i)
divisors = sorted(divisors)

ans = sum(divisors[bisect_left(divisors, x)] - x for x in lis)
print(ans)