def factorial_recursive(n):
    if n:
        return int(n) * factorial_recursive(n - 1)
    else:
        return 1

def combination(n, k):
    return factorial_recursive(n) // factorial_recursive(n - k) // factorial_recursive(k)

import sys
sys.setrecursionlimit(10000)

grid_width, grid_height, point_a_x, point_a_y, point_b_x, point_b_y = map(int, input().split())

delta_x = min(grid_width - abs(point_a_x - point_b_x), abs(point_a_x - point_b_x))
delta_y = min(grid_height - abs(point_a_y - point_b_y), abs(point_a_y - point_b_y))

result = 1
if delta_x * 2 == grid_width:
    result *= 2
if delta_y * 2 == grid_height:
    result *= 2
result *= combination(delta_x + delta_y, delta_x)
print(result % 100000007)