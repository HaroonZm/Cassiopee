import sys

for line in sys.stdin:
    if line.strip() == "":
        continue
    a, b, c, d, e, f = map(int, line.split())
    denom = a * e - b * d
    x = (c * e - b * f) / denom
    y = (a * f - c * d) / denom
    print(f"{x:.3f} {y:.3f}")