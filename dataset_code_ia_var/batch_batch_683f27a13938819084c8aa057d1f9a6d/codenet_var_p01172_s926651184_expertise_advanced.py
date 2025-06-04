from math import gcd
from sys import stdin

def multiplicative_order(n, m):
    if m == 1:
        return 0
    x, seen = 1, set()
    for k in range(1, m + 1):
        x = (x * n) % m
        if x == 1:
            return k
        if x in seen:
            break
        seen.add(x)
    return None

for line in stdin:
    if line.strip() == '0':
        break
    a, b = map(int, line.split())
    d = gcd(a, b)
    a, b = a // d, b // d

    cnt = 0
    while (g := gcd(b, 10)) != 1:
        b //= g
        cnt += 1

    print(cnt, multiplicative_order(10, b))