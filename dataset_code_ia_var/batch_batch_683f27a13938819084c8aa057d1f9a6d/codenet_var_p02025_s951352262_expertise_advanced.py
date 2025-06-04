from functools import reduce
from operator import mul

def f(): return map(int, input().split())

h, w = f()

def subarrays_sum(row, y):
    return sum(map(lambda xv: (xv[0] + 1) * (w - xv[0]) * xv[1], enumerate(row))) * (y + 1) * (h - y)

print(sum(subarrays_sum(list(f()), y) for y in range(h)))