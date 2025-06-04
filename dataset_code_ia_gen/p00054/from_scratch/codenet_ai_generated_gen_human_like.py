import sys

for line in sys.stdin:
    if line.strip() == '':
        continue
    a, b, n = map(int, line.split())
    s = 0
    r = a % b
    for _ in range(n):
        r *= 10
        digit = r // b
        r %= b
        s += digit
    print(s)