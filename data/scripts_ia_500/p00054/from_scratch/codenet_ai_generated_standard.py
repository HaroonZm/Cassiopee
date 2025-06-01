import sys

for line in sys.stdin:
    if not line.strip():
        continue
    a, b, n = map(int, line.split())
    r = a % b
    s = 0
    for _ in range(n):
        r *= 10
        d = r // b
        s += d
        r %= b
    print(s)