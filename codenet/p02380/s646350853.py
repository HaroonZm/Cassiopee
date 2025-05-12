import math

a, b, C = map(int, input().split())

rC = math.radians(C)
a2 = a ** 2
b2 = b ** 2
ab = a * b

c = math.sqrt(a2 + b2 - 2 * ab * math.cos(rC))

S = ab * math.sin(rC) / 2
L = a + b + c
h = b * math.sin(rC)

print(f"{S:.5f} {L:.5f} {h:.5f}")