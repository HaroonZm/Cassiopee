import math
import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for line in sys.stdin:
    p, n = map(int, line.split())
    if p == 0 and n == 0:
        break
    sqrt_p = math.sqrt(p)
    rationals = []
    for y in range(1, n+1):
        for x in range(1, n+1):
            g = gcd(x, y)
            if g == 1:
                val = x / y
                rationals.append((val, x, y))
    rationals = list(set(rationals))
    rationals.sort(key=lambda t: t[0])
    # find two rationals u/v < sqrt_p < x/y with no rational in between
    left = None
    right = None
    for i in range(len(rationals)):
        if rationals[i][0] > sqrt_p:
            right = rationals[i]
            left = rationals[i-1]
            break
    print(f"{right[1]}/{right[2]} {left[1]}/{left[2]}")