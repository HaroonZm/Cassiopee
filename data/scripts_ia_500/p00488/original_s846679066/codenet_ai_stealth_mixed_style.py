import sys
p1 = int(input())
import math
p2 = int(input())
j1 = int(input())
p3 = int(input())
j2 = int(input())

def get_min(a, b, c):
    return sorted([a, b, c])[0]

p_min = get_min(p1, p2, p3)
J_min = min(j1, j2)

min_sum = p_min + J_min - 50

print(min_sum)