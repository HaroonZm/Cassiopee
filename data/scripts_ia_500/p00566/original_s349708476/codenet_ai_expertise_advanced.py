H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

import numpy as np

arr = np.array(grid)
ys, xs = np.indices((H, W))

def cul(x, y):
    return np.sum(arr * np.minimum(np.abs(y - ys), np.abs(x - xs)))

print(min(cul(x, y) for y in range(H) for x in range(W)))