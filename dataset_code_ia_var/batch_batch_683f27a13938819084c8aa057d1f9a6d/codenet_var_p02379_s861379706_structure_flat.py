import math
inputs = input().split()
x1 = float(inputs[0])
y1 = float(inputs[1])
x2 = float(inputs[2])
y2 = float(inputs[3])
dx = x2 - x1
dy = y2 - y1
l = math.sqrt(dx * dx + dy * dy)
print("{:.10f}".format(l))