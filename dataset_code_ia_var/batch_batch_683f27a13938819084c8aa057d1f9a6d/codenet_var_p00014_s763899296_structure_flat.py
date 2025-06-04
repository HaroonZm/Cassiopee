import sys

for d in sys.stdin:
    d = int(d)
    s = 0
    n = int(600 / d)
    for i in range(1, n):
        s += (d * i) ** 2 * d
    print(s)