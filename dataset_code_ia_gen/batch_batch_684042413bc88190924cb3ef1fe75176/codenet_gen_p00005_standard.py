import sys
import math

for line in sys.stdin:
    if not line.strip():
        continue
    a, b = map(int, line.split())
    g = math.gcd(a, b)
    l = a // g * b
    print(g, l)