import math
import sys
input = sys.stdin.readline().rstrip

a, b, C = map(float, input().split())
C = math.radians(C)

S = a * b * math.sin(C) / 2
L = a + b + math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C))
h = b * math.sin(C)

print(S)
print(L)
print(h)