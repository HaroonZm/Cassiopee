import sys

def gcd_steps(a, b):
    steps = 0
    x, y = a, b
    while y != 0:
        x, y = y, x % y
        steps += 1
    return x, steps

for line in sys.stdin:
    a, b = map(int, line.split())
    if a == 0 and b == 0:
        break
    g, s = gcd_steps(a, b)
    print(g, s)