import sys

input_lines = sys.stdin.readlines()
lines = []
for line in input_lines:
    lines.append(line.strip())

n = int(lines[0])
lines = lines[1:]

for i in range(n):
    coords = lines[i].split(" ")
    x1 = float(coords[0])
    y1 = float(coords[1])
    x2 = float(coords[2])
    y2 = float(coords[3])
    x3 = float(coords[4])
    y3 = float(coords[5])
    x4 = float(coords[6])
    y4 = float(coords[7])

    X1 = x2 - x1
    Y1 = y2 - y1
    X2 = x4 - x3
    Y2 = y4 - y3

    if abs(X1 * Y2 - X2 * Y1) < 1e-10:
        print("YES")
    else:
        print("NO")