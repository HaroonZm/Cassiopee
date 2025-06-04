import sys

def rectangles_overlap(xa1, ya1, xa2, ya2, xb1, yb1, xb2, yb2):
    # rectangles overlap if they are not separated horizontally or vertically
    # Because touching is considered overlapping, use <= and >= for comparisons
    if xa2 < xb1 or xb2 < xa1:
        return False
    if ya2 < yb1 or yb2 < ya1:
        return False
    return True

for line in sys.stdin:
    if not line.strip():
        continue
    values = line.strip().split()
    if len(values) != 8:
        continue
    xa1, ya1, xa2, ya2, xb1, yb1, xb2, yb2 = map(float, values)

    # Normalize coordinates to ensure left-bottom < right-top for each rectangle
    xa1, xa2 = min(xa1, xa2), max(xa1, xa2)
    ya1, ya2 = min(ya1, ya2), max(ya1, ya2)
    xb1, xb2 = min(xb1, xb2), max(xb1, xb2)
    yb1, yb2 = min(yb1, yb2), max(yb1, yb2)

    if rectangles_overlap(xa1, ya1, xa2, ya2, xb1, yb1, xb2, yb2):
        print("YES")
    else:
        print("NO")