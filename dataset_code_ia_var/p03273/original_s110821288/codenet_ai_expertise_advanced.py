from sys import stdin
from itertools import compress

h, w = map(int, stdin.readline().split())
rows = [stdin.readline().rstrip() for _ in range(h)]

row_mask = [row.count('.') != w for row in rows]
col_mask = [any(row[i] != '.' for row in rows) for i in range(w)]

for row in compress(rows, row_mask):
    print(''.join(compress(row, col_mask)))