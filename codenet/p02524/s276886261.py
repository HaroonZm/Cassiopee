import math

numbers = input().strip().split()
numbers = list(map(float, numbers))
a = numbers[0]
b = numbers[1]
rad = numbers[2] / 180 * math.pi

h = b * math.sin(rad)
S = a * h / 2
c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(rad))
L = a + b + c

print("%.5f %.5f %.5f" % (S, L, h))