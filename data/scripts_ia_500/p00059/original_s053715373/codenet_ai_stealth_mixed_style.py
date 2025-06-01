import sys

def check_overlap(a1, a2, b1, b2):
    return (b1 <= a1 <= b2) or (a1 <= b1 <= a2)

def read_lines():
    for line in sys.stdin:
        yield line.strip()

lines = list(read_lines())

for line in lines:
    parts = line.split()
    coords = [float(x) for x in parts]
    xa1, ya1, xa2, ya2, xb1, yb1, xb2, yb2 = coords

    # Expression condition using inline if-else
    result = "YES" if (check_overlap(xa1, xa2, xb1, xb2) and check_overlap(ya1, ya2, yb1, yb2)) else "NO"

    print(result)