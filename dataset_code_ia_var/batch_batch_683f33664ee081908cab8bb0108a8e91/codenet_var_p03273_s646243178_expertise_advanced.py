from sys import stdin
from itertools import compress

h, w = map(int, stdin.readline().split())
a = [list(stdin.readline().rstrip()) for _ in range(h)]

row_mask = [any(cell != '.' for cell in row) for row in a]
col_mask = [any(a[i][j] != '.' for i in range(h)) for j in range(w)]

output = [
    ''.join(compress(row, col_mask))
    for row, flag in zip(a, row_mask) if flag
]

print(*output, sep='\n')