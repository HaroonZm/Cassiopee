import math
x1, x2, y1, y2 = map(float, raw_input().split())
a = y1 - x1
b = y2 - x2
c = math.pow(a, 2)
d = math.pow(b, 2)
e = c + d
f = math.sqrt(e)
print f