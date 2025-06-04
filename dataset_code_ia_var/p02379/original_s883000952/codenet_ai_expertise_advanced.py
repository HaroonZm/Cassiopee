from math import hypot

a, b, c, d = map(float, input().split())
print(f"{hypot(a - c, b - d):.8f}")