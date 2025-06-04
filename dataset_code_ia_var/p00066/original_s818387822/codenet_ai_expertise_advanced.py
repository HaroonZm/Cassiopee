import sys
from itertools import islice

def win(c, line):
    win_patterns = [
        (slice(0, 3), slice(3, 6), slice(6, 9)),  # rows
        (slice(0, 9, 3), slice(1, 9, 3), slice(2, 9, 3)),  # columns
        (slice(0, 9, 4),),  # main diagonal
        (slice(2, 7, 2),)   # anti-diagonal
    ]
    cells = tuple(line.strip())
    for row in range(3):
        if all(cells[i] == c for i in range(row * 3, row * 3 + 3)):
            return True
    for col in range(3):
        if all(cells[i] == c for i in range(col, 9, 3)):
            return True
    if all(cells[i] == c for i in range(0, 9, 4)):
        return True
    if all(cells[i] == c for i in range(2, 7, 2)):
        return True
    return False

for line in map(str.strip, sys.stdin):
    result = next((c for c in ('o', 'x') if win(c, line)), 'd')
    print(result)