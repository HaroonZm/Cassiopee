from math import sqrt, pow
x1, y1, x2, y2 = map(float, raw_input().split(' '))
print sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))