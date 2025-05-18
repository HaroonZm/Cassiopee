import math

n = int(input())
b = 100
for i in range(n):
  b += b * 0.05
  b = math.ceil(b)
b *= 1000
print("%d" % b)