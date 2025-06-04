from sys import stdin
import math

a, b = map(int, stdin.readline().split())
print(f"{divmod(a, b)[0]} {divmod(a, b)[1]} {a / b:.10f}")