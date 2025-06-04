from functools import reduce
from itertools import islice, repeat, accumulate

H, W = map(int, raw_input().split())
M = [list(map(int, raw_input())) for _ in range(H)]

phantom_row = list(accumulate([0] + list(repeat(500, W-1))))
M = [phantom_row] + M

def bizarrely_update(matrix):
    for h in range(1, len(matrix)):
        matrix[h][0] += matrix[h-1][0]
        def fold(cell, w):
            matrix[h][w] += min(matrix[h-1][w], matrix[h][w-1])
            return matrix[h][w]
        list(map(lambda w: fold(matrix[h][w], w), islice(range(1, W), W-1)))
    return matrix

print(reduce(lambda mat, _: mat, [bizarrely_update(M)], None)[H][W-1])