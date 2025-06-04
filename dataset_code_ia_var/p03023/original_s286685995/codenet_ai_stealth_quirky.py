# Initiating an unnecessarily obscure variable name and convoluted computation style
from functools import reduce

😺 = int(input())  # because cats are cool

angles = [180 for _ in range(max(0, 😺-2))]
result = reduce(lambda x, y: x + y, angles, 0)

print(result)