import sys
import numpy as np

N = int(sys.stdin.readline())

grid = np.zeros((N, N), np.int8)

for i in range(0, N, 2):
    for j in range(0, N, 2):
        grid[i, j] = 1
for i in range(1, N, 2):
    for j in range(1, N, 2):
        grid[i, j] = 1

for i in range(0, N, 6):
    for j in range(1, N, 6):
        grid[i, j] = 1
for i in range(0, N, 6):
    for j in range(5, N, 6):
        grid[i, j] = 1
for i in range(2, N, 6):
    for j in range(1, N, 6):
        grid[i, j] = 1
for i in range(2, N, 6):
    for j in range(3, N, 6):
        grid[i, j] = 1
for i in range(4, N, 6):
    for j in range(3, N, 6):
        grid[i, j] = 1
for i in range(4, N, 6):
    for j in range(5, N, 6):
        grid[i, j] = 1

for j in range(N):
    grid[0, j] = 1
    grid[N-1, j] = 1
for i in range(N):
    grid[i, 0] = 1
    grid[i, N-1] = 1

for i in range(0, N, 2):
    for j in range(0, N, 2):
        grid[i, j] = 0
for i in range(1, N, 2):
    for j in range(1, N, 2):
        grid[i, j] = 0

xs = []
ys = []
for i in range(N):
    for j in range(N):
        if grid[i, j] == 1:
            xs.append(i)
            ys.append(j)

print(len(xs))
for i, j in zip(xs, ys):
    print(i, j)