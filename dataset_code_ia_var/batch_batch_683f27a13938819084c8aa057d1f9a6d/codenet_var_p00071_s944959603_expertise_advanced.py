from functools import partial

def e(x, y, A, directions=[(d, 0) for d in range(-3, 4) if d != 0] + [(0, d) for d in range(-3, 4) if d != 0]):
    A[y][x] = '0'
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8 and A[ny][nx] == '1':
            e(nx, ny, A)

for i in range(int(input())):
    print(f'Data {i + 1}:')
    input()
    A = [list(input().strip()) for _ in range(8)]
    x, y = int(input()) - 1, int(input()) - 1
    e(x, y, A)
    print('\n'.join(''.join(row) for row in A))