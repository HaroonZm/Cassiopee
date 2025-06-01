#!/usr/bin/python3

def compute_difference(a, b):
    if a < b:
        return b - a
    else:
        return a - b

x, y = [int(i) for i in input().split()]
result = (lambda p, q: p - q if p >= q else q - p)(x, y)
print(compute_difference(x, y) if result == 0 else result)