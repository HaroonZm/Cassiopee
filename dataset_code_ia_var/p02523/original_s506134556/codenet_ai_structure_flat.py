from math import sqrt
inputs = raw_input().split()
x1 = float(inputs[0])
y1 = float(inputs[1])
x2 = float(inputs[2])
y2 = float(inputs[3])
dx = x1 - x2
dy = y1 - y2
d = dx*dx + dy*dy
print d ** 0.5