def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

import sys

for line in sys.stdin:
    if line.strip():
        x, y = map(int, line.split())
        print(gcd(x, y))