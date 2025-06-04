import sys
import numpy as np

n, m, x = map(int, sys.stdin.readline().split())
a = set(map(int, sys.stdin.readline().split()))

# Count elements in a >= x (right side), and < x (left side)
cost_left = sum(1 for pos in a if pos < x)
cost_right = sum(1 for pos in a if pos >= x)

print(min(cost_left, cost_right))