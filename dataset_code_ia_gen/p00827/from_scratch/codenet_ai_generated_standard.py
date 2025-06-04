import sys

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

for line in sys.stdin:
    a, b, d = map(int, line.split())
    if a == 0 and b == 0 and d == 0:
        break
    g, x0, y0 = extended_gcd(a, b)
    x0 *= d // g
    y0 *= d // g
    # general solution: x = x0 + k*(b/g), y = y0 - k*(a/g)
    A = b // g
    B = a // g

    # We want nonnegative x,y => x0 + k*A >=0 and y0 - k*B >=0
    # So k >= ceil(-x0 / A) and k <= floor(y0 / B)
    from math import ceil, floor
    k_min = ceil(-x0 / A) if A != 0 else 0
    k_max = floor(y0 / B) if B != 0 else 0

    best_x = None
    best_y = None
    best_sum = None
    best_mass = None

    for k in range(k_min, k_max +1):
        x = x0 + k * A
        y = y0 - k * B
        if x < 0 or y < 0:
            continue
        s = x + y
        m = a*x + b*y
        if best_sum is None or s < best_sum or (s == best_sum and m < best_mass):
            best_sum = s
            best_mass = m
            best_x = x
            best_y = y

    print(best_x, best_y)