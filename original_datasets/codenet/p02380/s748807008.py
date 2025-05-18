import math

a, b, c = [int(x) for x in input().split() ]

s = a * b * math.sin( math.radians(c)) / 2
l = a + b + math.sqrt(
    (b*math.sin(math.radians(c)))**2 + (a - b * math.cos(math.radians(c)))**2)

h = b * math.sin( math.radians(c))
print(s)
print(l)
print(h)