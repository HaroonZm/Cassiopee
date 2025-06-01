import sys

input_lines = sys.stdin.readlines()
lines = map(lambda x: x[:-1], input_lines)
lines = list(map(lambda x: x.split(" "), lines))
n = int(lines[0][0])
lines.pop(0)

for l in lines:
    x1, y1, x2, y2, x3, y3, x4, y4 = map(float, l)
    X1 = x2 - x1
    X2 = x4 - x3
    Y1 = y2 - y1
    Y2 = y4 - y3
    if abs(X1*Y2 - X2*Y1) < 1e-10:
        print("YES")
    else:
        print("NO")