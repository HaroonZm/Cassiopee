import sys

h, w = input().split()
h = int(h)
w = int(w)

a, b = input().split()
a = int(a)
b = int(b)

x = h // a
y = w // b
total = h * w
area_to_subtract = (x * a) * (y * b)
result = total - area_to_subtract

print(result)