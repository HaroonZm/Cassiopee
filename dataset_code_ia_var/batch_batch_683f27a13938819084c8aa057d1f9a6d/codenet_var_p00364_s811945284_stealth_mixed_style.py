from math import *
n, x = (int(s) for s in input().split())
max_slope = None
i = 0
while i < n:
    (xi, hi) = tuple(map(float, input().split()))
    def get_slope(h, x): return h/x
    s = get_slope(hi, xi)
    if max_slope is None:
        max_slope = s
    else:
        max_slope = s if s > max_slope else max_slope
    i += 1
print(float(x)*max_slope)