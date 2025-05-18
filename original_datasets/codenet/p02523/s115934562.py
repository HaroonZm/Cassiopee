from math import sqrt, pow
def dist(x1, y1, x2, y2):
  return sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

x1, y1, x2, y2 = map(float, raw_input().split(' '))
print dist(x1, y1, x2, y2)