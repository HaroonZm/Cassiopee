import sys

H, W, D = map(int, sys.stdin.readline().split())

grid = []
for i in range(H):
    row = []
    for j in range(W):
        plus = (i + j) // D % 2
        minus = (i - j) // D % 2
        x = plus + 2 * minus

        if x == 0:
            c = 'R'
        elif x == 1:
            c = 'B'
        elif x == 2:
            c = 'G'
        else:
            c = 'Y'
        row.append(c)
    grid.append(row)

for row in grid:
    print(''.join(row))