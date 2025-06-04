import numpy as np
import math

n = int(input())
a = []
total = 0

for i in range(n):
    a.append(np.array(list(map(int, input().split()))))

for i in range(n):
    for s in range(i, n):
        total += np.linalg.norm(a[s] - a[i])

print(total * 2 / n)