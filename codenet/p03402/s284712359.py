B, A = map(int, input().split())

h, w = 100, 100
grid = [['.'] * 100 for _ in range(50)] + [['#'] * 100 for _ in range(50)]

for i in range(A - 1):
    A1, A2 = divmod(i, 50)
    grid[2 * A1][2 * A2] = '#'

for j in range(B - 1):
    B1, B2 = divmod(j, 50)
    grid[2 * B1 + 51][2 * B2] = '.'

print(h, w)
for i in range(100):
    print(''.join(grid[i]))