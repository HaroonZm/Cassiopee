import sys
from itertools import starmap

r = d = 0
for line in sys.stdin:
    try:
        a, b, c = map(int, map(str.strip, line.split(',')))
    except ValueError:
        continue
    d += a == b
    r += a * a + b * b == c * c

print(r)
print(d)