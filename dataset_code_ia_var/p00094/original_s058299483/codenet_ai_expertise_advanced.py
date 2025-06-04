from sys import stdin
from operator import mul

a, b = map(int, stdin.readline().split())
print(f"{mul(a, b) / 3.305785:.6f}")