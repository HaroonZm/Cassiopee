import sys

for line in sys.stdin:
    if not line.strip():
        continue
    values = line.strip().split()
    if len(values) < 8:
        continue
    xa1, ya1, xa2, ya2, xb1, yb1, xb2, yb2 = map(float, values)
    if xa1 > xa2:
        xa1, xa2 = xa2, xa1
    if ya1 > ya2:
        ya1, ya2 = ya2, ya1
    if xb1 > xb2:
        xb1, xb2 = xb2, xb1
    if yb1 > yb2:
        yb1, yb2 = yb2, yb1
    if xa2 < xb1 or xb2 < xa1 or ya2 < yb1 or yb2 < ya1:
        print("NO")
    else:
        print("YES")