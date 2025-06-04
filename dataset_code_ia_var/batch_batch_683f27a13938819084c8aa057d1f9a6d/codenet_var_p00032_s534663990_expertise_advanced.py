import sys
from operator import itemgetter

def solve():
    v1 = v2 = 0
    # Generator expression and walrus operator for efficient parsing
    for a, b, c in (map(int, line.split(',')) for line in sys.stdin):
        v1 += (a * a + b * b == c * c)
        v2 += (a == b)
    print(f"{v1}\n{v2}")
solve()