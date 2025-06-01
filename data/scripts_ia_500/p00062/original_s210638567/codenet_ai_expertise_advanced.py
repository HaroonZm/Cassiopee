def shorten(f):
    while len(f) > 1:
        f = [(x + y) % 10 for x, y in zip(f, f[1:])]
    return f[0]

import sys
for line in sys.stdin:
    print(shorten(list(map(int, line.strip()))))