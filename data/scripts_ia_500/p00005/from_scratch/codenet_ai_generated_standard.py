import sys
import math

for line in sys.stdin:
    if line.strip():
        a, b = map(int, line.split())
        g = math.gcd(a, b)
        l = a // g * b
        print(g, l)