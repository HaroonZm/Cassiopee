import math
inputs = input().split()
x1 = float(inputs[0])
y1 = float(inputs[1])
x2 = float(inputs[2])
y2 = float(inputs[3])
dx = x1 - x2
dy = y1 - y2
dx2 = dx * dx
dy2 = dy * dy
sum_sq = dx2 + dy2
distance = math.sqrt(sum_sq)
print(distance)