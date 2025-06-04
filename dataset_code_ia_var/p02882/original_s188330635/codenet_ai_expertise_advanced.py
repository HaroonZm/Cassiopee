import math
from functools import partial

def calc_factory(a, b):
    return lambda t: (a * a * b - a * a * a * math.tan(t) / 2
                      if a * math.tan(t) <= b
                      else b * b * a / (2 * math.tan(t)))

def binary_search(f, target, lo=0., hi=90., tol=1e-10, max_iter=50):
    for _ in range(max_iter):
        mid = (lo + hi) / 2
        v = f(math.radians(mid))
        if v < target:
            hi = mid
        else:
            lo = mid
        if abs(hi - lo) < tol:
            break
    return mid

a, b, x = map(int, input().split())
calc = calc_factory(a, b)
result = binary_search(calc, x)
print(result)