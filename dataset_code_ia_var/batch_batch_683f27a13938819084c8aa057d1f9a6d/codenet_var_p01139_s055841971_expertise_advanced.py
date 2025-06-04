import sys
from collections import Counter
from functools import partial

sys.setrecursionlimit(2502)

def paint(field, i, j, b, f, h, w, moves=((-1,0), (1,0), (0,1), (0,-1))):
    stack = [(i, j)]
    while stack:
        x, y = stack.pop()
        fij = field[x][y]
        if fij & f or (fij & 4 and not fij & b):
            continue
        field[x][y] |= b | f
        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < h and 0 <= ny < w:
                stack.append((nx, ny))

buf = []
chardict = {'.': 0, 'W': 5, 'B': 6}
while True:
    try:
        w, h = map(int, input().split())
    except Exception:
        break
    if w == 0:
        break
    field = [list(map(chardict.get, input())) for _ in range(h)]
    for i, row in enumerate(field):
        for j, cell in enumerate(row):
            if cell & 4 and not cell & 24:
                paint(field, i, j, cell & 3, (cell & 3) << 3, h, w)
    result = Counter(b & 7 for row in field for b in row)
    print(result[2], result[1])