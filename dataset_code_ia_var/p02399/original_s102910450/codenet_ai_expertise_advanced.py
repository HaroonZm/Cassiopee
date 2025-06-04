from sys import stdin
from operator import truediv, floordiv, mod

a, b = map(int, stdin.readline().split())

print(f"{floordiv(a, b)} {mod(a, b)} {truediv(a, b):.6f}")